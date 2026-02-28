"""Sportradar DataCore API Client
Handles authentication, token management, and API requests.
Provides methods to access various endpoints.

Author: Michael Adams, 2025
"""

import logging
import time
from threading import RLock
from types import TracebackType
from typing import Any, TypeVar
from uuid import UUID

import httpx
from datacore_client import AuthenticatedClient
from datacore_client.types import UNSET, Unset

from sportradar_datacore_api.errors import (
    AuthenticationError,
    NotFoundError,
    TransportError,
    UnexpectedResponseError,
    ValidationError,
)

logger = logging.getLogger(__name__)

T = TypeVar("T")


class DataCoreAPI:
    """
    OAuth2-authenticated wrapper for Sportradar DataCore.
    Handles token acquisition, caching, and renewal.
    """

    _TOKEN_BUFFER = 60  # seconds before actual expiry to refresh

    def __init__(  # noqa: PLR0913
        self,
        base_url: str,
        auth_url: str,
        client_id: str,
        client_secret: str,
        sport: str,
        org_id: str | None = None,
        scopes: list[str] | None = None,
        timeout: int = 5,
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

        self._token: str | None = None
        self._expires_at: float = 0.0
        self._lock = RLock()

        self.client: AuthenticatedClient | None = None

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
            raise TransportError(f"Authentication failed: {e}") from e

        data = response.json().get("data", {})
        self._token = data.get("token")
        if not self._token:
            raise AuthenticationError("Token missing in authentication response.")

        logger.debug("Authenticated successfully")

        expires_in = data.get("expires_in", 3600)
        self._expires_at = time.time() + expires_in - self._TOKEN_BUFFER
        self.session.headers.update({"Authorization": f"Bearer {self._token}"})

        if self.client is not None:
            self.client.token = self._token

    def _ensure_token(self) -> None:
        with self._lock:
            if not self._token or time.time() >= self._expires_at:
                logger.info("Refreshing access token")
                self._authenticate()

    def _ensure_client(self) -> AuthenticatedClient:
        with self._lock:
            self._ensure_token()
            if self._token is None:
                raise AuthenticationError("Authentication token was not initialized.")
            token = self._token
            if self.client is None:
                self.client = AuthenticatedClient(
                    base_url=self.base_url,
                    token=token,
                    verify_ssl=True,  # enforce SSL in production
                    raise_on_unexpected_status=True,
                    timeout=httpx.Timeout(self.timeout),
                )
            else:
                self.client.token = token
            return self.client

    @staticmethod
    def _require_value(name: str, value: str) -> None:
        if not value:
            raise ValidationError(f"{name} must be provided.")

    @staticmethod
    def _as_uuid(value: str | UUID, name: str) -> UUID:
        if isinstance(value, UUID):
            return value
        try:
            return UUID(str(value))
        except ValueError as exc:
            raise ValidationError(f"{name} must be a valid UUID.") from exc

    @staticmethod
    def _as_offset(offset: int | None) -> int | Unset:
        return UNSET if offset is None else offset

    @staticmethod
    def _uuid_to_str(value: UUID | Unset | None, name: str) -> str:
        if value is None or isinstance(value, Unset):
            raise NotFoundError(f"{name} is missing in response.")
        return str(value)

    def _unwrap_response(self, parsed: Any, success_type: type[T], context: str) -> T:
        if parsed is None:
            raise UnexpectedResponseError(f"{context}: empty response")
        if isinstance(parsed, success_type):
            return parsed
        raise UnexpectedResponseError(f"{context}: API error: {parsed}")

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "DataCoreAPI":
        self._ensure_client()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
