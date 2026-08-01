"""Tests for explicit and environment-based client configuration."""

import pytest

from sportradar_datacore_api.api import DataCoreAPI
from sportradar_datacore_api.errors import ValidationError

EXPECTED_TIMEOUT = 10


def test_constructor_does_not_authenticate() -> None:
    api = DataCoreAPI(
        base_url="https://api.example.com",
        auth_url="https://auth.example.com/token",
        client_id="client",
        client_secret="secret",
        sport="handball",
    )

    assert api.client is None
    assert api._token is None
    api.close()


def test_from_env_creates_lazy_client(monkeypatch: pytest.MonkeyPatch) -> None:
    values = {
        "BASE_URL": "https://api.example.com",
        "AUTH_URL": "https://auth.example.com/token",
        "CLIENT_ID": "client",
        "CLIENT_SECRET": "secret",
        "CLIENT_ORGANIZATION_ID": "organization",
        "SPORT": "handball",
        "DATACORE_SCOPES": "read:organization,read:fixtures",
        "DATACORE_TIMEOUT": "10",
    }
    for name, value in values.items():
        monkeypatch.setenv(name, value)

    api = DataCoreAPI.from_env(dotenv_path="does-not-exist.env")

    assert api.base_url == values["BASE_URL"]
    assert api.auth_url == values["AUTH_URL"]
    assert api.scopes == ["read:organization", "read:fixtures"]
    assert api.timeout == EXPECTED_TIMEOUT
    assert api.client is None
    api.close()


def test_from_env_reports_missing_required_variables(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("BASE_URL", raising=False)

    with pytest.raises(ValidationError, match="BASE_URL"):
        DataCoreAPI.from_env(dotenv_path="does-not-exist.env")
