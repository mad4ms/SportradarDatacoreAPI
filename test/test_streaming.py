"""Tests for the separate DataCore streaming client."""

import os
import types

import pytest
from dotenv import load_dotenv

from sportradar_datacore_api.errors import ValidationError
from sportradar_datacore_api.stream_models import StreamAccessGrant, StreamTopicGrant
from sportradar_datacore_api.stream_utils import (
    decode_compressed_data,
    decode_stream_message,
)
from sportradar_datacore_api.streaming import HandballStreamClient, HandballStreamingAPI

DEFAULT_KEEPALIVE = 15
DEFAULT_TLS_PORT = 443

COMPRESSED_SAMPLE = "eJyrVkrLz1eyUkpKLFKqBQAdegQ0"


def test_decode_compressed_data_roundtrip() -> None:
    decoded = decode_compressed_data(COMPRESSED_SAMPLE)
    assert decoded == {"foo": "bar"}


def test_decode_stream_message_includes_decoded_compressed_data() -> None:
    payload = '{"type":"statistics","compressedData":"' + COMPRESSED_SAMPLE + '"}'

    message = decode_stream_message("topic/one", payload)

    assert message.topic == "topic/one"
    assert message.message_type == "statistics"
    assert message.decoded_compressed_data == {"foo": "bar"}
    assert isinstance(message.payload, dict)
    assert message.payload["decodedCompressedData"] == {"foo": "bar"}


def test_stream_access_read_topics_filter_catchup_and_response() -> None:
    grant = StreamAccessGrant(
        url="wss://example.com/mqtt",
        client_id="stream-client",
        topics=(
            StreamTopicGrant("topic/read", "read:stream_events", "read"),
            StreamTopicGrant("topic/catchup", "read:stream_persons_catchup", "read"),
            StreamTopicGrant("topic/response", "read:response", "read"),
            StreamTopicGrant("topic/write", "write:stream_events", "write"),
        ),
    )

    selected = grant.read_topics(include_catchup=False, include_response=False)
    assert selected == ["topic/read"]


def test_streaming_api_derives_token_base_from_auth_url() -> None:
    stream_api = HandballStreamingAPI(
        client_id="client",
        client_secret="secret",
        sport="handball",
        auth_url="https://token.connect.sportradar.com/v1/oauth2/rest/token",
    )

    assert stream_api.token_base_url == "https://token.connect.sportradar.com/v1"
    stream_api.close()


def test_streaming_api_requires_token_base_or_auth_url() -> None:
    with pytest.raises(ValidationError):
        HandballStreamingAPI(
            client_id="client",
            client_secret="secret",
            sport="handball",
        )


def test_handball_stream_client_subscribes_only_selected_topics(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    subscribed: list[tuple[str, int]] = []

    class FakeClient:
        def __init__(self, *args: object, **kwargs: object) -> None:
            self.args = args
            self.kwargs = kwargs
            self.ws_options: tuple[str, dict[str, str]] | None = None
            self.on_connect = None
            self.on_disconnect = None
            self.on_message = None

        def tls_set(self) -> None:
            return None

        def ws_set_options(self, *, path: str, headers: dict[str, str]) -> None:
            self.ws_options = (path, headers)

        def subscribe(self, topic: str, qos: int = 0) -> None:
            subscribed.append((topic, qos))

        def connect(self, host: str, port: int, keepalive: int) -> None:
            assert host == "example.com"
            assert port == DEFAULT_TLS_PORT
            assert keepalive == DEFAULT_KEEPALIVE

        def disconnect(self) -> None:
            return None

        def loop_start(self) -> None:
            return None

        def loop_stop(self) -> None:
            return None

        def publish(
            self,
            topic: str,
            payload: object,
            qos: int = 0,
            retain: bool = False,
        ) -> object:
            del topic, payload, qos, retain
            return types.SimpleNamespace(mid=1, rc=0)

    fake_mqtt = types.SimpleNamespace(
        CallbackAPIVersion=types.SimpleNamespace(VERSION2=object()),
        Client=FakeClient,
    )

    monkeypatch.setattr(
        "sportradar_datacore_api.streaming.mqtt",
        fake_mqtt,
    )

    grant = StreamAccessGrant(
        url="wss://example.com/mqtt?token=abc",
        client_id="stream-client",
        topics=(
            StreamTopicGrant("topic/read", "read:stream_events", "read"),
            StreamTopicGrant(
                "topic/catchup",
                "read:stream_persons_catchup",
                "read",
            ),
            StreamTopicGrant("topic/response", "read:response", "read"),
            StreamTopicGrant("topic/write", "write:stream_events", "write"),
        ),
    )

    client = HandballStreamClient(
        grant,
        include_catchup=False,
        include_response=False,
    )

    client.connect()
    client.subscribe_granted_topics(qos=1)

    assert subscribed == [("topic/read", 1)]


@pytest.fixture(scope="module")
def live_stream_api() -> HandballStreamingAPI:
    load_dotenv(".env", override=True)

    required = ["CLIENT_ID", "CLIENT_SECRET"]
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        pytest.skip(
            "Missing required environment variables for streaming tests: "
            + ", ".join(missing)
        )

    stream_token_base_url = os.getenv("STREAM_TOKEN_BASE_URL")
    auth_url = os.getenv("AUTH_URL")
    if not stream_token_base_url and not auth_url:
        pytest.skip("Missing STREAM_TOKEN_BASE_URL or AUTH_URL for streaming tests.")

    return HandballStreamingAPI(
        client_id=os.getenv("CLIENT_ID", ""),
        client_secret=os.getenv("CLIENT_SECRET", ""),
        sport="handball",
        token_base_url=stream_token_base_url,
        auth_url=auth_url,
    )


def test_fixture_stream_access_live(live_stream_api: HandballStreamingAPI) -> None:
    fixture_id = os.getenv("STREAM_FIXTURE_ID")
    if not fixture_id:
        pytest.skip("Missing STREAM_FIXTURE_ID for live streaming access test.")
    assert fixture_id is not None

    access = live_stream_api.get_fixture_access(
        fixture_id,
        ["read:stream_events", "read:stream_status"],
    )

    assert access.url.startswith("wss://")
    assert access.client_id
