"""Handball API wrapper for Sportradar DataCore API.
Handles authentication, token management, and API requests.
Provides methods to access handball-related endpoints.

Author: Michael Adams, 2025
"""

import csv
import json
import logging
from typing import Any, Dict, List

from datacore_client.api.competitions import competition_list
from datacore_client.api.match_play_by_play import fixture_pbp_export
from datacore_client.api.matches import fixture_list
from datacore_client.api.seasons import season_list
from datacore_client.models import (
    CompetitionListResponseDefault,
    FixtureListResponseDefault,
    FixturePbpExportResponseDefault,
    SeasonListResponseDefault,
)

from sportradar_datacore_api.api import DataCoreAPI


class HandballAPI(DataCoreAPI):
    """
    Unified API wrapper for handball-related endpoints.
    Provides access to organizations, leagues, competitions,
    entities, persons, fixtures, etc.
    """

    # --- Public helpers requested -----------------------------------------

    def get_competition_id_by_name(self, competition_name: str) -> str:
        """
        Resolve a competition UUID by human-friendly name.
        Tries exact (case-insensitive) match on common name fields, then 'contains'.
        """
        # Efficiently fetch competitions with a higher limit to reduce API calls

        resp = competition_list.sync_detailed(
            client=self.client,
            organization_id=self.org_id,
            name_local_contains=competition_name,  # Filter for Bundesliga competitions
            limit=50,  # Increase limit for efficiency if expecting many results
        )

        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")

        parsed = resp.parsed
        if isinstance(parsed, CompetitionListResponseDefault):
            competitions = list(parsed.data or [])  # list[CompetitionModel]
            for c in competitions:
                comp_id = c.competition_id

                if c.name_local and c.name_local.lower() == competition_name.lower():
                    return comp_id
        else:
            # Default/error schema from API (typed)
            err: CompetitionListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_season_id_by_year(self, competition_id: str, season_year: int) -> str:
        """
        Resolve a season UUID by name under a given competition.
        Tries exact (case-insensitive) match on common name fields, then 'contains'.
        """
        response = season_list.sync_detailed(
            client=self.client,
            organization_id=self.org_id,
            competition_id=competition_id,
            limit=200,
        )

        if response.status_code == 200:
            logging.info("Seasons fetched successfully.")
            logging.debug("Status Code: %s", response.status_code)
            parsed = response.parsed
            if isinstance(parsed, SeasonListResponseDefault):
                seasons = list(parsed.data or [])

                for c in seasons:
                    season_id = c.season_id

                    logging.debug("Checking season: %s (%s)", c.name_local, season_id)

                    if c.year == season_year:
                        return season_id
            else:
                err: SeasonListResponseDefault = parsed
                raise RuntimeError(f"API error: {err}")

    def get_list_matches_by_season_id(self, season_id: str) -> List[Dict[str, Any]]:
        """
        Return all fixtures (matches) for the given season as a list of dicts.
        """
        if not season_id:
            raise ValueError("season_id must be provided.")
        resp = fixture_list.sync_detailed(
            client=self.client,
            organization_id=self.org_id,
            season_id=season_id,
            limit=500,  # Adjust limit as needed
        )

        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")

        parsed = resp.parsed

        if isinstance(parsed, FixtureListResponseDefault):
            return parsed.data or []
        else:
            err: FixtureListResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def get_fixture_events_by_id(self, fixture_id: str) -> Dict[str, Any]:
        """
        Return the full fixture (match) metadata for a given fixture ID.
        """
        if not fixture_id:
            raise ValueError("fixture_id must be provided.")
        resp = fixture_pbp_export.sync_detailed(
            client=self.client,
            organization_id=self.org_id,
            fixture_id=fixture_id,
        )

        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")
        parsed = resp.parsed
        if isinstance(parsed, FixturePbpExportResponseDefault):
            content_dict = json.loads(resp.content)
            return content_dict.get("data") or {}
        else:
            err: FixturePbpExportResponseDefault = parsed
            raise RuntimeError(f"API error: {err}")

    def save_events_to_csv(self, events: List[dict], file_path: str) -> None:
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
            if isinstance(event, dict) and "data" in event:
                data_rows.append(event["data"])
            elif isinstance(event, dict):
                data_rows.append(event)

        if not data_rows:
            logging.error("No event data found to save.")
            return

        # Collect all keys for CSV header
        fieldnames = set()
        for row in data_rows:
            if isinstance(row, dict):
                fieldnames.update(row.keys())
        fieldnames = sorted(fieldnames)

        with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_rows:
                if isinstance(row, dict):
                    writer.writerow(row)

        logging.debug("Events saved to %s", file_path)
