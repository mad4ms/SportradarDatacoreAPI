"""Configuration helpers for the Sportradar DataCore API."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from sportradar_datacore_api.errors import ValidationError


@dataclass(frozen=True, slots=True)
class DataCoreSettings:
    """Explicit configuration required to create a DataCore API client."""

    base_url: str
    auth_url: str
    client_id: str
    client_secret: str
    sport: str = "handball"
    org_id: str | None = None
    scopes: tuple[str, ...] = ("read:organization",)
    timeout: int = 5

    @classmethod
    def from_env(
        cls,
        *,
        dotenv_path: str | Path | None = None,
    ) -> "DataCoreSettings":
        """Load settings from environment variables and an optional dotenv file."""
        load_dotenv(dotenv_path)

        def required(name: str) -> str:
            value = os.getenv(name)
            if not value:
                raise ValidationError(f"Environment variable {name} must be provided.")
            return value

        scopes_value = os.getenv("DATACORE_SCOPES", "read:organization")
        scopes = tuple(
            scope.strip() for scope in scopes_value.split(",") if scope.strip()
        )
        if not scopes:
            raise ValidationError("DATACORE_SCOPES must contain at least one scope.")

        timeout_value = os.getenv("DATACORE_TIMEOUT", "5")
        try:
            timeout = int(timeout_value)
        except ValueError as exc:
            raise ValidationError("DATACORE_TIMEOUT must be an integer.") from exc
        if timeout <= 0:
            raise ValidationError("DATACORE_TIMEOUT must be greater than zero.")

        return cls(
            base_url=required("BASE_URL"),
            auth_url=required("AUTH_URL"),
            client_id=required("CLIENT_ID"),
            client_secret=required("CLIENT_SECRET"),
            sport=os.getenv("SPORT", "handball"),
            org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
            scopes=scopes,
            timeout=timeout,
        )
