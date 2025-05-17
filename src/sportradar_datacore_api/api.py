"""Sportradar DataCore API Client
Handles authentication, token management, and API requests.
Provides methods to access various endpoints.
"""

from typing import Any, Dict, Optional, List
import time
import requests


class APIAuthenticationError(Exception):
    """Exception raised for authentication errors."""

    pass


class APIRequestError(Exception):
    """Exception raised for request errors."""

    pass


class DataCoreAPI:
    """
    OAuth2-authenticated wrapper for Sportradar DataCore.
    Handles token acquisition, caching, renewal, and rate-limiting.
    """

    _TOKEN_BUFFER = 60  # seconds before actual expiry to refresh

    def __init__(
        self,
        base_url: str,
        auth_url: str,
        client_id: str,
        client_secret: str,
        sport: str,
        org_id: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        timeout: int = 5,
        rate_limit_sleep: float = 1.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.sport = sport
        self.org_id = org_id
        self.scopes = scopes or ["read:organization"]
        self.timeout = timeout
        self.rate_limit_sleep = rate_limit_sleep

        self._token: Optional[str] = None
        self._expires_at: float = 0.0

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def _authenticate(self) -> None:
        payload: Dict[str, Any] = {
            "credentialId": self.client_id,
            "credentialSecret": self.client_secret,
            "sport": self.sport,
            "organization": {"id": [self.org_id]} if self.org_id else None,
            "scopes": self.scopes,
        }
        payload = {k: v for k, v in payload.items() if v is not None}

        try:
            response = self.session.post(
                self.auth_url, json=payload, timeout=self.timeout
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise APIAuthenticationError(f"Authentication failed: {e}") from e

        data = response.json().get("data", {})
        self._token = data.get("token")
        if not self._token:
            raise APIAuthenticationError(
                "Token missing in authentication response."
            )

        expires_in = data.get("expires_in", 3600)
        self._expires_at = time.time() + expires_in - self._TOKEN_BUFFER
        self.session.headers.update({"Authorization": f"Bearer {self._token}"})

    def _ensure_token(self) -> None:
        if not self._token or time.time() >= self._expires_at:
            self._authenticate()

    def _make_request(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        self._ensure_token()
        time.sleep(self.rate_limit_sleep)

        url = (
            endpoint
            if endpoint.startswith("http")
            else f"{self.base_url}/{endpoint.lstrip('/')}"
        )
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                params=params or {},
                json=json,
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise APIRequestError(f"Request failed: {e}") from e

        return response.json()
