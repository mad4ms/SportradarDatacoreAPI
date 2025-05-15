from typing import List, Optional, Any, Dict
from sportradar_datacore_api.api import DataCoreAPI


class HandballAPI(DataCoreAPI):
    """Unified API wrapper for handball-related endpoints."""

    def get_organizations(self, params: Optional[Dict[str, Any]] = None) -> List[dict]:
        return self._safe_request(f"{self.base_url}/handball/organizations", params)

    def get_organization(self) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/organizations/{self.org_id}"
        )

    def get_leagues(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/leagues", params
        )

    def get_competitions(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/competitions", params
        )

    def get_competition(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/competitions/{competition_id}",  # noqa
            params,
        )  # noqa

    def get_conferences(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/conferences", params
        )

    def get_clubs(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/entityGroups", params
        )

    def get_club(
        self, entity_group_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/entityGroups/{entity_group_id}",
            params,
        )

    def get_teams(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/entities", params
        )

    def get_team(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/entities/{entity_id}", params
        )

    def get_persons(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/persons", params
        )

    def get_person(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/persons/{person_id}", params
        )

    def get_seasons(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            (
                f"{self.base_url}/handball/o/{self.org_id}/competitions/"
                f"{competition_id}/seasons"
            ),
            params,
        )

    def get_season(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/{season_id}", params
        )

    def get_season_persons(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/{season_id}/persons",
            params,
        )

    def get_person_seasons(
        self, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/persons/{person_id}",
            params,
        )

    def get_season_person(
        self, season_id: str, person_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            (
                f"{self.base_url}/handball/o/{self.org_id}/seasons/"
                f"{season_id}/persons/{person_id}"
            ),
            params,
        )

    def get_season_teams(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/{season_id}/entities",
            params,
        )

    def get_team_seasons(
        self, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/entities/{entity_id}",
            params,
        )

    def get_season_team(
        self, season_id: str, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            (
                f"{self.base_url}/handball/o/{self.org_id}/seasons/"
                f"{season_id}/entities/{entity_id}"
            ),
            params,
        )

    def get_all_season_teams(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/entities", params
        )

    def get_season_fixtures(
        self, season_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get a list of matches (fixtures) for a given season.
        """
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/{season_id}/fixtures",
            params,
        )

    def get_fixture(
        self, fixture_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Return detailed information about a specific match.
        """
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/fixtures/{fixture_id}",
            params,
        )

    def get_season_team_fixtures(
        self, season_id: str, entity_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get a list of matches for a specific team within a season.
        """
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/seasons/{season_id}/entities/{entity_id}/fixtures",  # noqa
            params,
        )

    def get_competition_fixtures(
        self, competition_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get a list of matches for a specific competition.
        """
        return self._safe_request(
            f"{self.base_url}/handball/o/{self.org_id}/competitions/{competition_id}/fixtures", # noqa
            params,
        )

    def _safe_request(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        try:
            return self._make_request(endpoint=endpoint, params=params or {})
        except Exception as e:
            print(f"API call failed for {endpoint}: {e}")
            return {}
