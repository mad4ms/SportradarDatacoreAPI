"""Sportradar DataCore API Client
Handles authentication, token management, and API requests.
Provides methods to access various endpoints.

Author: Michael Adams, 2025
"""

import logging
import time
from typing import Any, Optional

import httpx
from datacore_client import AuthenticatedClient

logger = logging.getLogger(__name__)


class APIAuthenticationError(Exception):
    """Exception raised for authentication errors."""


class APIRequestError(Exception):
    """Exception raised for request errors."""


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
        scopes: Optional[list[str]] = None,
        timeout: int = 5,
        rate_limit_sleep: float = 1.0,
        connect_on_init: bool = True,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.sport = sport
        self.org_id = org_id
        self.scopes: list[str] = scopes or ["read:organization"]
        self.timeout = timeout
        self.rate_limit_sleep = rate_limit_sleep

        self._token: Optional[str] = None
        self._expires_at: float = 0.0

        self.client: Optional[AuthenticatedClient] = None

        self.session = httpx.Client()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        if connect_on_init:
            self.connect()

    def connect(
        self,
    ) -> None:
        self._ensure_client()

    def _authenticate(self) -> None:
        payload: dict[str, Any] = {
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
        except httpx.HTTPError as e:
            raise APIAuthenticationError(f"Authentication failed: {e}") from e

        data = response.json().get("data", {})
        self._token = data.get("token")
        if not self._token:
            raise APIAuthenticationError("Token missing in authentication response.")

        logger.debug("Authenticated successfully")

        expires_in = data.get("expires_in", 3600)
        self._expires_at = time.time() + expires_in - self._TOKEN_BUFFER
        self.session.headers.update({"Authorization": f"Bearer {self._token}"})

        if self.client is not None:
            self.client.token = self._token

    def _ensure_token(self) -> None:
        if not self._token or time.time() >= self._expires_at:
            logger.info("Refreshing access token")
            self._authenticate()

    def _ensure_client(self) -> AuthenticatedClient:
        self._ensure_token()
        if self.client is None:
            self.client = AuthenticatedClient(
                base_url=self.base_url,
                token=self._token,
                verify_ssl=True,  # enforce SSL in production
                raise_on_unexpected_status=True,
            )
        else:
            self.client.token = self._token
        return self.client

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "DataCoreAPI":
        self._ensure_client()
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        self.close()
