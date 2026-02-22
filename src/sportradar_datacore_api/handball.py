"""Handball API wrapper for Sportradar DataCore API.
Handles authentication, token management, and API requests.
Provides methods to access handball-related endpoints.

Author: Michael Adams, 2025
"""

import csv
import json
import logging
import uuid
from collections.abc import Mapping, Sequence
from typing import Any

from datacore_client.api.competitions import competition_list
from datacore_client.api.match_persons import fixture_persons_list
from datacore_client.api.match_play_by_play import fixture_pbp_export
from datacore_client.api.matches import fixture_detail, fixture_list
from datacore_client.api.persons import person_list
from datacore_client.api.season_persons import season_persons_list
from datacore_client.api.season_teams import season_entities_list
from datacore_client.api.seasons import season_list
from datacore_client.api.teams import entity_detail

# from datacore_client.api.teams import entity_list
from datacore_client.models import (
    CompetitionListCompetitionsResponse,
    CompetitionListResponseDefault,
    EntityDetailEntitiesResponse,
    EntityDetailResponseDefault,
    FixtureDetailFixturesResponse,
    FixtureDetailResponseDefault,
    FixtureListFixturesResponse,
    FixtureListResponseDefault,
    FixturePbpExportResponseDefault,
    FixturePbpExportSuccessResponse,
    FixturePersonsListFixturePersonsResponse,
    FixturePersonsListResponseDefault,
    PersonListPersonsResponse,
    PersonListResponseDefault,
    SeasonEntitiesListResponseDefault,
    SeasonEntitiesListSeasonEntitiesListResponse,
    SeasonListResponseDefault,
    SeasonListSeasonsResponse,
    SeasonPersonsListResponseDefault,
    SeasonPersonsListSeasonPersonsListResponse,
)

from sportradar_datacore_api.api import DataCoreAPI

logger = logging.getLogger(__name__)


class HandballAPI(DataCoreAPI):
    """
    Unified API wrapper for handball-related endpoints.
    Provides access to organizations, leagues, competitions,
    entities, persons, fixtures, etc.
    """

    # --- Public helpers requested -----------------------------------------

    @staticmethod
    def _require_value(name: str, value: str) -> None:
        if not value:
            raise ValueError(f"{name} must be provided.")

    @staticmethod
    def _ensure_ok(response: Any, context: str) -> None:
        if response.status_code != 200:
            raise RuntimeError(
                f"{context}: HTTP {response.status_code}: {response.content!r}"
            )

    @classmethod
    def _to_plain(cls, value: Any) -> Any:
        if isinstance(value, list):
            return [cls._to_plain(item) for item in value]
        if isinstance(value, dict):
            return {key: cls._to_plain(item) for key, item in value.items()}
        if hasattr(value, "model_dump"):
            return value.model_dump()
        if hasattr(value, "to_dict"):
            return value.to_dict()
        return value

    @classmethod
    def _json_data_from_response(cls, response: Any, context: str) -> Any:
        try:
            payload = json.loads(response.content)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{context}: invalid JSON response") from exc
        if not isinstance(payload, dict):
            raise RuntimeError(f"{context}: unexpected JSON shape")
        return cls._to_plain(payload.get("data"))

    @staticmethod
    def _normalize_fixture_id(item: Mapping[str, Any]) -> dict[str, Any]:
        data = dict(item)
        if "fixtureId" in data and "fixture_id" not in data:
            data["fixture_id"] = data["fixtureId"]
        if "fixture_id" in data and "fixtureId" not in data:
            data["fixtureId"] = data["fixture_id"]
        return data

    @staticmethod
    def _log_request(context: str, **details: Any) -> None:
        request_id = uuid.uuid4().hex
        logger.debug("%s request_id=%s details=%s", context, request_id, details)

    def get_competition_id_by_name(
        self,
        competition_name: str,
        *,
        limit: int = 50,
        offset: int | None = None,
    ) -> str:
        """
        Resolve a competition UUID by human-friendly name.
        Tries exact (case-insensitive) match on common name fields, then 'contains'.
        """
        # Efficiently fetch competitions with a higher limit to reduce API calls

        self._require_value("competition_name", competition_name)

        self._log_request(
            "competition_list",
            competition_name=competition_name,
            limit=limit,
            offset=offset,
        )

        resp = competition_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            name_local_contains=competition_name,  # Filter for Bundesliga competitions
            limit=limit,  # Increase limit for efficiency if expecting many results
            hide_null=True,  # Avoid null UUID fields that break model parsing
            offset=offset,
        )

        self._ensure_ok(resp, "competition_list")

        parsed = resp.parsed
        if isinstance(parsed, CompetitionListCompetitionsResponse):
            competitions = list(parsed.data or [])
            for c in competitions:
                if (
                    c.name_local
                    and c.name_local.casefold() == competition_name.casefold()
                ):
                    return c.competition_id
            raise LookupError(f"No competition found matching '{competition_name}'.")
        else:
            # Default/error schema from API (typed)
            err: CompetitionListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_season_id_by_year(
        self,
        competition_id: str,
        season_year: int,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> str:
        """
        Resolve a season UUID by name under a given competition.
        Tries exact (case-insensitive) match on common name fields, then 'contains'.
        """
        self._require_value("competition_id", competition_id)

        self._log_request(
            "season_list",
            competition_id=competition_id,
            season_year=season_year,
            limit=limit,
            offset=offset,
        )

        response = season_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            competition_id=competition_id,
            limit=limit,
            offset=offset,
        )

        self._ensure_ok(response, "season_list")
        logger.info("Seasons fetched successfully.")
        logger.debug("Status Code: %s", response.status_code)
        parsed = response.parsed
        if isinstance(parsed, SeasonListSeasonsResponse):
            seasons = list(parsed.data or [])

            for c in seasons:
                logging.debug("Checking season: %s (%s)", c.name_local, c.season_id)

                if c.year == season_year:
                    return c.season_id

            raise LookupError(
                f"No season found for competition '{competition_id}' in {season_year}."
            )
        else:
            err: SeasonListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_teams_by_season_id(
        self,
        season_id: str,
        *,
        limit: int = 100,
        offset: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Return all teams for the given season as a list of dicts.
        """
        self._require_value("season_id", season_id)

        self._log_request(
            "season_entities_list",
            season_id=season_id,
            limit=limit,
            offset=offset,
        )
        resp = season_entities_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            season_id=season_id,
            include="entities,organizations",
            limit=limit,
            offset=offset,
            # fields=
        )

        self._ensure_ok(resp, "season_entities_list")

        parsed = resp.parsed

        if isinstance(parsed, SeasonEntitiesListSeasonEntitiesListResponse):
            return self._to_plain(parsed.data or [])
        else:
            err: SeasonEntitiesListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_players_by_season_id(
        self,
        season_id: str,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Return all players for the given season as a list of dicts.
        """
        self._require_value("season_id", season_id)

        self._log_request(
            "season_persons_list",
            season_id=season_id,
            limit=limit,
            offset=offset,
        )
        resp = season_persons_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            season_id=season_id,
            include="entities,organizations",
            limit=limit,
            offset=offset,
        )

        self._ensure_ok(resp, "season_persons_list")

        parsed = resp.parsed

        if isinstance(parsed, SeasonPersonsListSeasonPersonsListResponse):
            players: list[Any] = []
            for entry in list(parsed.data or []):
                if entry.players:
                    players.extend(entry.players)
            return self._to_plain(players)
        else:
            err: SeasonPersonsListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_players_by_match_id(
        self,
        match_id: str,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Return all players for the given match as a list of dicts.
        """
        self._require_value("match_id", match_id)

        self._log_request(
            "fixture_persons_list",
            match_id=match_id,
            limit=limit,
            offset=offset,
        )
        resp = fixture_persons_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            fixture_id=match_id,
            limit=limit,
            offset=offset,
        )

        self._ensure_ok(resp, "fixture_persons_list")

        parsed = resp.parsed

        if isinstance(parsed, FixturePersonsListFixturePersonsResponse):
            players: list[Any] = []
            for entry in list(parsed.data or []):
                if entry.players:
                    players.extend(entry.players)
            return self._to_plain(players)
        else:
            err: FixturePersonsListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_list_matches_by_season_id(
        self,
        season_id: str,
        *,
        limit: int = 500,
        offset: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Return all fixtures (matches) for the given season as a list of dicts.
        """
        self._require_value("season_id", season_id)

        self._log_request(
            "fixture_list",
            season_id=season_id,
            limit=limit,
            offset=offset,
        )
        resp = fixture_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            season_id=season_id,
            external="entityId,personId",
            include="organizations,entities",
            limit=limit,
            offset=offset,
        )

        self._ensure_ok(resp, "fixture_list")

        parsed = resp.parsed

        if isinstance(parsed, FixtureListFixturesResponse):
            fixtures = self._to_plain(parsed.data or [])
            return [
                self._normalize_fixture_id(item) if isinstance(item, Mapping) else item
                for item in fixtures
            ]
        else:
            err: FixtureListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_team_by_id(self, entity_id: str) -> dict[str, Any]:
        """
        Return the full entity (team) metadata for a given entity ID.
        """
        self._require_value("entity_id", entity_id)

        self._log_request("entity_detail", entity_id=entity_id)
        resp = entity_detail.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            entity_id=entity_id,
            include="entities,organizations",
        )
        self._ensure_ok(resp, "entity_detail")
        parsed = resp.parsed
        if isinstance(parsed, EntityDetailEntitiesResponse):
            return self._to_plain(parsed.data or {})
        else:
            err: EntityDetailResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_fixture_by_id(self, fixture_id: str) -> dict[str, Any]:
        """
        Return the full fixture (match) metadata for a given fixture ID.
        """
        self._require_value("fixture_id", fixture_id)

        self._log_request("fixture_detail", fixture_id=fixture_id)
        resp = fixture_detail.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            fixture_id=fixture_id,
            include="entities,organizations,persons",
            external="entityId,personId",
            hide_null=False,
            limit=1000,
        )

        self._ensure_ok(resp, "fixture_detail")
        parsed = resp.parsed
        if isinstance(parsed, FixtureDetailFixturesResponse):
            data = self._to_plain(parsed.data or {})
            if isinstance(data, Mapping):
                return self._normalize_fixture_id(data)
            return data
        else:
            err: FixtureDetailResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_fixture_events_by_id(
        self, fixture_id: str, setup_only: bool, with_scores: bool
    ) -> list[dict[str, Any]]:
        """
        Return the fixture events for a given fixture ID.
        """
        self._require_value("fixture_id", fixture_id)

        self._log_request(
            "fixture_pbp_export",
            fixture_id=fixture_id,
            setup_only=setup_only,
            with_scores=with_scores,
        )
        resp = fixture_pbp_export.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            fixture_id=fixture_id,
            limit=1000,
            only_setup=setup_only,
            with_scores=with_scores,
        )

        self._ensure_ok(resp, "fixture_pbp_export")
        parsed = resp.parsed
        if isinstance(parsed, FixturePbpExportSuccessResponse):
            data = self._json_data_from_response(resp, "fixture_pbp_export")
            if data is None:
                return []
            if not isinstance(data, list):
                raise RuntimeError("fixture_pbp_export: unexpected data shape")
            return data
        else:
            err: FixturePbpExportResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_players_by_ids(
        self, person_ids: str, *, limit: int = 500, offset: int | None = None
    ) -> list[dict[str, Any]]:
        """
        Return the full player metadata for given player IDs (comma-separated).
        """
        self._require_value("person_ids", person_ids)

        self._log_request(
            "person_list",
            person_ids=person_ids,
            limit=limit,
            offset=offset,
        )
        resp = person_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=self.org_id,
            person_ids=person_ids,
            limit=limit,
            offset=offset,
        )

        self._ensure_ok(resp, "person_list")
        parsed = resp.parsed
        if isinstance(parsed, PersonListPersonsResponse):
            data = self._json_data_from_response(resp, "person_list")
            if data is None:
                return []
            if not isinstance(data, list):
                raise RuntimeError("person_list: unexpected data shape")
            return data
        else:
            err: PersonListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def save_events_to_csv(
        self, events: Sequence[Mapping[str, Any]], file_path: str
    ) -> None:
        """
        Save a list of event dicts (from a single fixture) to a CSV file.
        Each row in the CSV will represent one event's 'data' field.
        """
        if not events:
            raise ValueError("events must be provided.")
        if not file_path:
            raise ValueError("file_path must be provided.")

        # Extract the 'data' field from each event if present
        data_rows = []
        for event in events:
            if isinstance(event, Mapping) and "data" in event:
                data_rows.append(event["data"])
            elif isinstance(event, Mapping):
                data_rows.append(event)
            else:
                logging.warning("Skipping non-mapping event: %r", event)

        if not data_rows:
            logging.error("No event data found to save.")
            return

        # Collect all keys for CSV header
        fieldnames: set[str] = set()
        for row in data_rows:
            if isinstance(row, Mapping):
                fieldnames.update(row.keys())
        fieldnames = sorted(fieldnames)

        with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_rows:
                if isinstance(row, Mapping):
                    writer.writerow(row)

        logging.debug("Events saved to %s", file_path)
