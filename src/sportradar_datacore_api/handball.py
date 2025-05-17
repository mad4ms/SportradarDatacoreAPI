"""Handball API wrapper for Sportradar DataCore API.
Handles authentication, token management, and API requests.
Provides methods to access handball-related endpoints.
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
        path = "/".join(
            ["handball", "o", self.org_id] + [p.strip("/") for p in parts if p]
        )
        return self._make_request(
            f"{self.base_url}/{path}", params=params or {}
        )

    def get_organizations(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._make_request(
            f"{self.base_url}/handball/organizations", params=params or {}
        )

    def get_organization(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("organizations", self.org_id, params=params)

    def get_leagues(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("leagues", params=params)

    def get_competitions(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("competitions", params=params)

    def get_competition(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("competitions", competition_id, params=params)

    def get_conferences(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("conferences", params=params)

    def get_clubs(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("entityGroups", params=params)

    def get_club(
        self, entity_group_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("entityGroups", entity_group_id, params=params)

    def get_teams(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("entities", params=params)

    def get_team(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("entities", entity_id, params=params)

    def get_persons(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("persons", params=params)

    def get_person(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("persons", person_id, params=params)

    def get_seasons(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get(
            "competitions", competition_id, "seasons", params=params
        )

    def get_season(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", season_id, params=params)

    def get_season_persons(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", season_id, "persons", params=params)

    def get_person_seasons(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", "persons", person_id, params=params)

    def get_season_person(
        self,
        season_id: str,
        person_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return self._get(
            "seasons", season_id, "persons", person_id, params=params
        )

    def get_season_teams(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", season_id, "entities", params=params)

    # https://developer.connect.sportradar.com/datacore/handball_rest.html#tag/Season-Teams/operation/season_entity_list # noqa
    def get_team_seasons(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", "entities", entity_id, params=params)

    def get_season_team(
        self,
        season_id: str,
        entity_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return self._get(
            "seasons", season_id, "entities", entity_id, params=params
        )

    def get_all_season_teams(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", "entities", params=params)

    def get_season_fixtures(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("seasons", season_id, "fixtures", params=params)

    def get_fixture(
        self, fixture_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._get("fixtures", fixture_id, params=params)

    def get_season_team_fixtures(
        self,
        season_id: str,
        entity_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
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
        return self._get(
            "competitions", competition_id, "fixtures", params=params
        )

    def get_playbyplay(
        self, fixture_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get play-by-play records for a match (fixture).
        """
        return self._get("fixtures", fixture_id, "playbyplay", params=params)
