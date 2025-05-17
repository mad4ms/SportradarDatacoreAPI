"""Handball API wrapper for Sportradar DataCore API.
Handles authentication, token management, and API requests.
Provides methods to access handball-related endpoints.

Author: Michael Adams, 2025
"""

from typing import Any, Dict, Optional
from sportradar_datacore_api.api import DataCoreAPI


class HandballAPI(DataCoreAPI):
    """
    Unified API wrapper for handball-related endpoints.
    Provides access to organizations, leagues, competitions, entities, persons, fixtures, etc.
    """

    def _get(
        self, *parts: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Internal helper to construct and execute GET requests with organization context."""
        path = "/".join(
            ["handball", "o", self.org_id] + [p.strip("/") for p in parts if p]
        )
        return self._make_request(
            f"{self.base_url}/{path}", params=params or {}
        )

    def get_organizations(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all handball organizations."""
        return self._make_request(
            f"{self.base_url}/handball/organizations", params=params or {}
        )

    def get_organization(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of the current organization."""
        return self._get("organizations", self.org_id, params=params)

    def get_leagues(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all leagues under the organization."""
        return self._get("leagues", params=params)

    def get_competitions(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all competitions under the organization."""
        return self._get("competitions", params=params)

    def get_competition(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific competition."""
        return self._get("competitions", competition_id, params=params)

    def get_conferences(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all conferences under the organization."""
        return self._get("conferences", params=params)

    def get_clubs(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all clubs (entity groups)."""
        return self._get("entityGroups", params=params)

    def get_club(
        self, entity_group_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific club."""
        return self._get("entityGroups", entity_group_id, params=params)

    def get_teams(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all teams (entities)."""
        return self._get("entities", params=params)

    def get_team(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific team."""
        return self._get("entities", entity_id, params=params)

    def get_persons(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all persons."""
        return self._get("persons", params=params)

    def get_person(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific person."""
        return self._get("persons", person_id, params=params)

    def get_seasons(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List seasons of a competition."""
        return self._get(
            "competitions", competition_id, "seasons", params=params
        )

    def get_season(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific season."""
        return self._get("seasons", season_id, params=params)

    def get_season_persons(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List persons participating in a season."""
        return self._get("seasons", season_id, "persons", params=params)

    def get_person_seasons(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List seasons associated with a person."""
        return self._get("seasons", "persons", person_id, params=params)

    def get_season_person(
        self,
        season_id: str,
        person_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get season-specific data for a person."""
        return self._get(
            "seasons", season_id, "persons", person_id, params=params
        )

    def get_season_teams(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List teams participating in a season."""
        return self._get("seasons", season_id, "entities", params=params)

    def get_team_seasons(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List seasons in which a team participated."""
        return self._get("seasons", "entities", entity_id, params=params)

    def get_season_team(
        self,
        season_id: str,
        entity_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get data for a specific team in a specific season."""
        return self._get(
            "seasons", season_id, "entities", entity_id, params=params
        )

    def get_all_season_teams(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all season-team mappings."""
        return self._get("seasons", "entities", params=params)

    def get_season_fixtures(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all fixtures of a season."""
        return self._get("seasons", season_id, "fixtures", params=params)

    def get_fixture(
        self, fixture_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get details of a specific fixture (match)."""
        return self._get("fixtures", fixture_id, params=params)

    def get_season_team_fixtures(
        self,
        season_id: str,
        entity_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """List all fixtures for a team in a season."""
        return self._get(
            "seasons",
            season_id,
            "entities",
            entity_id,
            "fixtures",
            params=params,
        )

    def get_competition_fixtures(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """List all fixtures of a competition."""
        return self._get(
            "competitions", competition_id, "fixtures", params=params
        )

    def get_playbyplay(
        self, fixture_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Retrieve detailed play-by-play data for a fixture."""
        return self._get("fixtures", fixture_id, "playbyplay", params=params)
