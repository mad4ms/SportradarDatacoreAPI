"""Handball API wrapper for Sportradar DataCore API.
Handles authentication, token management, and API requests.
Provides methods to access handball-related endpoints.

Author: Michael Adams, 2025
"""

import json
import logging
import uuid
from collections.abc import Sequence
from typing import Any, cast
from uuid import UUID

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
    CompetitionModel,
    EntityDetailEntitiesResponse,
    FixtureDetailFixturesResponse,
    FixtureListFixturesResponse,
    FixturePbpExportSuccessResponse,
    FixturePersonsListFixturePersonsResponse,
    MatchModel,
    MatchPersonsModel,
    PersonListPersonsResponse,
    PersonModel,
    SeasonEntitiesListSeasonEntitiesListResponse,
    SeasonEntitiesModel,
    SeasonListSeasonsResponse,
    SeasonModel,
    SeasonPersonsListSeasonPersonsListResponse,
    SeasonPersonsModel,
    TeamModel,
)
from datacore_client.types import Unset

from sportradar_datacore_api.api import DataCoreAPI
from sportradar_datacore_api.errors import (
    NotFoundError,
    UnexpectedResponseError,
    ValidationError,
)

logger = logging.getLogger(__name__)
HTTP_OK = 200


class HandballAPI(DataCoreAPI):
    """
    Unified API wrapper for handball-related endpoints.
    Provides access to organizations, leagues, competitions,
    entities, persons, fixtures, etc.
    """

    # --- Public helpers requested -----------------------------------------

    def _require_org_id(self) -> str:
        if not self.org_id:
            raise ValidationError("org_id must be provided.")
        return self.org_id

    @staticmethod
    def _ensure_ok(response: Any, context: str) -> None:
        if response.status_code != HTTP_OK:
            raise UnexpectedResponseError(
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
            raise UnexpectedResponseError(f"{context}: invalid JSON response") from exc
        if not isinstance(payload, dict):
            raise UnexpectedResponseError(f"{context}: unexpected JSON shape")
        return cls._to_plain(payload.get("data"))

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

        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)

        resp = competition_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            name_local_contains=competition_name,  # Filter for Bundesliga competitions
            limit=limit,  # Increase limit for efficiency if expecting many results
            hide_null=True,  # Avoid null UUID fields that break model parsing
            offset=offset_value,
        )

        self._ensure_ok(resp, "competition_list")

        parsed = self._unwrap_response(
            resp.parsed,
            CompetitionListCompetitionsResponse,
            "competition_list",
        )
        data = parsed.data
        competitions: list[CompetitionModel] = (
            [] if isinstance(data, Unset) else list(data)
        )
        for c in competitions:
            if isinstance(c.name_local, str) and (
                c.name_local.casefold() == competition_name.casefold()
            ):
                return self._uuid_to_str(c.competition_id, "competition_id")
        raise NotFoundError(f"No competition found matching '{competition_name}'.")

    def get_season_id_by_year(
        self,
        competition_id: str | UUID,
        season_year: int,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> str:
        """
        Resolve a season UUID by name under a given competition.
        Tries exact (case-insensitive) match on common name fields, then 'contains'.
        """
        self._require_value("competition_id", str(competition_id))
        competition_uuid = self._as_uuid(competition_id, "competition_id")

        self._log_request(
            "season_list",
            competition_id=str(competition_uuid),
            season_year=season_year,
            limit=limit,
            offset=offset,
        )

        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)

        response = season_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            competition_id=competition_uuid,
            limit=limit,
            offset=offset_value,
        )

        self._ensure_ok(response, "season_list")
        logger.info("Seasons fetched successfully.")
        logger.debug("Status Code: %s", response.status_code)
        parsed = self._unwrap_response(
            response.parsed, SeasonListSeasonsResponse, "season_list"
        )
        data = parsed.data
        seasons: list[SeasonModel] = [] if isinstance(data, Unset) else list(data)

        for c in seasons:
            logger.debug("Checking season: %s (%s)", c.name_local, c.season_id)

            if c.year == season_year:
                return self._uuid_to_str(c.season_id, "season_id")

        raise NotFoundError(
            f"No season found for competition '{competition_uuid}' in {season_year}."
        )

    def get_teams_by_season_id(
        self,
        season_id: str | UUID,
        *,
        limit: int = 100,
        offset: int | None = None,
    ) -> list[SeasonEntitiesModel]:
        """
        Return all teams for the given season.
        """
        self._require_value("season_id", str(season_id))
        season_uuid = self._as_uuid(season_id, "season_id")

        self._log_request(
            "season_entities_list",
            season_id=str(season_uuid),
            limit=limit,
            offset=offset,
        )
        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)
        resp = season_entities_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            season_id=season_uuid,
            include="entities,organizations",
            limit=limit,
            offset=offset_value,
            # fields=
        )

        self._ensure_ok(resp, "season_entities_list")

        parsed = self._unwrap_response(
            resp.parsed,
            SeasonEntitiesListSeasonEntitiesListResponse,
            "season_entities_list",
        )
        data = parsed.data
        if isinstance(data, Unset):
            return []
        return list(data)

    def get_players_by_season_id(
        self,
        season_id: str | UUID,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> list[SeasonPersonsModel]:
        """
        Return all players for the given season.
        """
        self._require_value("season_id", str(season_id))
        season_uuid = self._as_uuid(season_id, "season_id")

        self._log_request(
            "season_persons_list",
            season_id=str(season_uuid),
            limit=limit,
            offset=offset,
        )
        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)
        resp = season_persons_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            season_id=season_uuid,
            include="entities,organizations",
            limit=limit,
            offset=offset_value,
        )

        self._ensure_ok(resp, "season_persons_list")

        parsed = self._unwrap_response(
            resp.parsed,
            SeasonPersonsListSeasonPersonsListResponse,
            "season_persons_list",
        )
        data = parsed.data
        if isinstance(data, Unset):
            return []
        return list(data)

    def list_players_by_match(
        self,
        match_id: str | UUID,
        *,
        limit: int = 200,
        offset: int | None = None,
    ) -> list[MatchPersonsModel]:
        """
        Return all players for the given match.
        """
        self._require_value("match_id", str(match_id))
        fixture_uuid = self._as_uuid(match_id, "match_id")

        self._log_request(
            "fixture_persons_list",
            match_id=str(fixture_uuid),
            limit=limit,
            offset=offset,
        )
        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)
        resp = fixture_persons_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            fixture_id=fixture_uuid,
            limit=limit,
            offset=offset_value,
        )

        self._ensure_ok(resp, "fixture_persons_list")

        parsed = self._unwrap_response(
            resp.parsed,
            FixturePersonsListFixturePersonsResponse,
            "fixture_persons_list",
        )
        data = parsed.data
        if isinstance(data, Unset):
            return []
        return list(data)

    def list_matches_by_season(
        self,
        season_id: str | UUID,
        *,
        limit: int = 500,
        offset: int | None = None,
    ) -> list[MatchModel]:
        """
        Return all matches for the given season.
        """
        self._require_value("season_id", str(season_id))
        season_uuid = self._as_uuid(season_id, "season_id")

        self._log_request(
            "fixture_list",
            season_id=str(season_uuid),
            limit=limit,
            offset=offset,
        )
        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)
        resp = fixture_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            season_id=season_uuid,
            external="entityId,personId",
            include="organizations,entities",
            limit=limit,
            offset=offset_value,
        )

        self._ensure_ok(resp, "fixture_list")

        parsed = self._unwrap_response(
            resp.parsed, FixtureListFixturesResponse, "fixture_list"
        )
        data = parsed.data
        if isinstance(data, Unset):
            return []
        return list(data)

    def get_team_by_id(self, entity_id: str | UUID) -> TeamModel:
        """
        Return the full entity (team) metadata for a given entity ID.
        """
        self._require_value("entity_id", str(entity_id))
        entity_uuid = self._as_uuid(entity_id, "entity_id")

        self._log_request("entity_detail", entity_id=str(entity_uuid))
        organization_id = self._require_org_id()
        resp = entity_detail.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            entity_id=entity_uuid,
            include="entities,organizations",
        )
        self._ensure_ok(resp, "entity_detail")
        parsed = self._unwrap_response(
            resp.parsed, EntityDetailEntitiesResponse, "entity_detail"
        )
        data = parsed.data
        if isinstance(data, Unset) or not data:
            raise NotFoundError(f"No team found for entity '{entity_uuid}'.")
        return data[0]

    def get_match_by_id(self, match_id: str | UUID) -> MatchModel:
        """
        Return the full match metadata for a given match ID.
        """
        self._require_value("match_id", str(match_id))
        fixture_uuid = self._as_uuid(match_id, "match_id")

        self._log_request("fixture_detail", fixture_id=str(fixture_uuid))
        organization_id = self._require_org_id()
        resp = fixture_detail.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            fixture_id=fixture_uuid,
            include="entities,organizations,persons",
            external="entityId,personId",
            hide_null=False,
            limit=1000,
        )

        self._ensure_ok(resp, "fixture_detail")
        parsed = self._unwrap_response(
            resp.parsed, FixtureDetailFixturesResponse, "fixture_detail"
        )
        data = parsed.data
        if isinstance(data, Unset) or not data:
            raise NotFoundError(f"No fixture found for id '{fixture_uuid}'.")
        return data[0]

    def get_match_events(
        self, match_id: str | UUID, setup_only: bool, with_scores: bool
    ) -> list[dict[str, Any]]:
        """
        Return the match events for a given match ID.
        """
        self._require_value("match_id", str(match_id))
        fixture_uuid = self._as_uuid(match_id, "match_id")

        self._log_request(
            "fixture_pbp_export",
            fixture_id=str(fixture_uuid),
            setup_only=setup_only,
            with_scores=with_scores,
        )
        organization_id = self._require_org_id()
        resp = fixture_pbp_export.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            fixture_id=fixture_uuid,
            limit=1000,
            only_setup=setup_only,
            with_scores=with_scores,
        )

        self._ensure_ok(resp, "fixture_pbp_export")
        self._unwrap_response(
            resp.parsed, FixturePbpExportSuccessResponse, "fixture_pbp_export"
        )
        data = self._json_data_from_response(resp, "fixture_pbp_export")
        if data is None:
            return []
        if not isinstance(data, list):
            raise UnexpectedResponseError("fixture_pbp_export: unexpected data shape")
        return data

    def get_players_by_ids(
        self,
        person_ids: str | Sequence[str | UUID],
        *,
        limit: int = 500,
        offset: int | None = None,
    ) -> list[PersonModel]:
        """
        Return the full player metadata for given player IDs (comma-separated).
        """
        if isinstance(person_ids, str):
            ids_list = [item.strip() for item in person_ids.split(",") if item.strip()]
        else:
            ids_list = [str(item) for item in person_ids if str(item).strip()]
        ids_text = ",".join(ids_list)
        self._require_value("person_ids", ids_text)

        self._log_request(
            "person_list",
            person_ids=ids_text,
            limit=limit,
            offset=offset,
        )
        organization_id = self._require_org_id()
        offset_value = self._as_offset(offset)
        person_id_arg: Any
        if len(ids_list) == 1:
            try:
                person_id_arg = self._as_uuid(ids_list[0], "person_ids")
            except ValidationError:
                person_id_arg = cast(Any, ids_text)
        else:
            person_id_arg = cast(Any, ids_text)
        resp = person_list.sync_detailed(
            client=self._ensure_client(),
            organization_id=organization_id,
            person_ids=person_id_arg,
            limit=limit,
            offset=offset_value,
        )

        self._ensure_ok(resp, "person_list")
        parsed = self._unwrap_response(
            resp.parsed, PersonListPersonsResponse, "person_list"
        )
        data = parsed.data
        if isinstance(data, Unset):
            return []
        return list(data)
