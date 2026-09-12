"""The generated client pins its Authorization header at construction time.

A token change therefore has to replace the client. These tests exercise that
invariant directly — no HTTP, no transport mocking: the constructor performs no
network I/O, and a pre-set expiry keeps `_ensure_client` from authenticating.
"""

import time

from sportradar_datacore_api.api import DataCoreAPI


def _api() -> DataCoreAPI:
    return DataCoreAPI(
        base_url="https://api.example.invalid/v1",
        auth_url="https://token.example.invalid/token",
        client_id="client-id",
        client_secret="client-secret",
        sport="handball",
    )


def test_token_change_replaces_the_generated_client() -> None:
    api = _api()
    api._token = "token-1"
    api._expires_at = time.time() + 3600

    first = api._ensure_client()
    first_transport = first.get_httpx_client()
    assert first_transport.headers["Authorization"] == "Bearer token-1"

    # Exactly what _authenticate() does once a fresh token arrives.
    api._token = "token-2"
    api._discard_client()

    second = api._ensure_client()
    assert second is not first
    assert second.get_httpx_client().headers["Authorization"] == "Bearer token-2"
    assert first_transport.is_closed, "the superseded transport must be closed"


def test_client_survives_when_the_token_is_unchanged() -> None:
    api = _api()
    api._token = "token-1"
    api._expires_at = time.time() + 3600

    first = api._ensure_client()
    assert api._ensure_client() is first


def test_close_releases_the_generated_client() -> None:
    api = _api()
    api._token = "token-1"
    api._expires_at = time.time() + 3600

    transport = api._ensure_client().get_httpx_client()
    api.close()

    assert transport.is_closed
    assert api.client is None
