"""Separate client for the Sportradar DataCore streaming API."""

import json
from collections.abc import Callable, Sequence
from importlib import import_module
from types import TracebackType
from typing import Protocol
from urllib.parse import urlparse

import httpx

from sportradar_datacore_api.errors import (
    DependencyError,
    TransportError,
    UnexpectedResponseError,
    ValidationError,
)
from sportradar_datacore_api.stream_models import (
    StreamAccessGrant,
    StreamMessage,
    StreamPublishResult,
    StreamTopicGrant,
)
from sportradar_datacore_api.stream_utils import decode_stream_message


def _load_mqtt_module() -> object | None:
    try:
        return import_module("paho.mqtt.client")
    except ModuleNotFoundError:
        return None


mqtt = _load_mqtt_module()


StreamMessageHandler = Callable[[StreamMessage], None]
StreamConnectHandler = Callable[[], None]
StreamDisconnectHandler = Callable[[int], None]


class MQTTPublishInfoProtocol(Protocol):
    """Minimal publish result surface used by the wrapper."""

    mid: int | None
    rc: int | None


class MQTTClientProtocol(Protocol):
    """Minimal MQTT client surface used by the wrapper."""

    on_connect: Callable[..., None] | None
    on_disconnect: Callable[..., None] | None
    on_message: Callable[..., None] | None

    def tls_set(self) -> None: ...

    def ws_set_options(self, *, path: str, headers: dict[str, str]) -> None: ...

    def connect(self, host: str, port: int, keepalive: int) -> None: ...

    def disconnect(self) -> None: ...

    def loop_start(self) -> None: ...

    def loop_stop(self) -> None: ...

    def subscribe(self, topic: str, qos: int = 0) -> object: ...

    def publish(
        self,
        topic: str,
        payload: bytes | str,
        qos: int = 0,
        retain: bool = False,
    ) -> MQTTPublishInfoProtocol: ...


class HandballStreamClient:
    """Websocket MQTT client for the DataCore streaming API."""

    def __init__(  # noqa: PLR0913
        self,
        access_grant: StreamAccessGrant,
        *,
        keepalive: int = 15,
        auto_subscribe: bool = True,
        include_catchup: bool = True,
        include_response: bool = True,
        on_message: StreamMessageHandler | None = None,
        on_connect: StreamConnectHandler | None = None,
        on_disconnect: StreamDisconnectHandler | None = None,
    ) -> None:
        self.access_grant = access_grant
        self.keepalive = keepalive
        self.auto_subscribe = auto_subscribe
        self.include_catchup = include_catchup
        self.include_response = include_response
        self._on_message_handler = on_message
        self._on_connect_handler = on_connect
        self._on_disconnect_handler = on_disconnect

        self._client: MQTTClientProtocol = self._build_client()
        self._configure_websocket_options()
        self._client.on_connect = self._handle_connect
        self._client.on_disconnect = self._handle_disconnect
        self._client.on_message = self._handle_message
        self._loop_started = False

    def _build_client(self) -> MQTTClientProtocol:
        if mqtt is None:
            raise DependencyError(
                "Streaming support requires paho-mqtt. Install the 'stream' extra."
            )

        client_factory = getattr(mqtt, "Client", None)
        if client_factory is None:
            raise DependencyError("Installed paho-mqtt package is missing Client.")

        callback_api_version = getattr(mqtt, "CallbackAPIVersion", None)
        if callback_api_version is None:
            client = client_factory(
                client_id=self.access_grant.client_id,
                transport="websockets",
            )
        else:
            version2 = getattr(callback_api_version, "VERSION2", None)
            if version2 is None:
                client = client_factory(
                    client_id=self.access_grant.client_id,
                    transport="websockets",
                )
            else:
                client = client_factory(
                    version2,
                    client_id=self.access_grant.client_id,
                    transport="websockets",
                )

        client.tls_set()
        return client

    def _configure_websocket_options(self) -> None:
        parsed_url = urlparse(self.access_grant.url)
        host = parsed_url.hostname
        if not host:
            raise ValidationError("Streaming access URL must include a hostname.")

        request_path = parsed_url.path or "/mqtt"
        if parsed_url.query:
            request_path = f"{request_path}?{parsed_url.query}"

        headers = {"host": host, "Host": host}
        self._client.ws_set_options(path=request_path, headers=headers)

    @property
    def host(self) -> str:
        parsed_url = urlparse(self.access_grant.url)
        host = parsed_url.hostname
        if not host:
            raise ValidationError("Streaming access URL must include a hostname.")
        return host

    @property
    def port(self) -> int:
        parsed_url = urlparse(self.access_grant.url)
        return parsed_url.port or 443

    def connect(self) -> None:
        self._client.connect(self.host, self.port, self.keepalive)

    def disconnect(self) -> None:
        self._client.disconnect()

    def loop_start(self) -> None:
        if not self._loop_started:
            self._client.loop_start()
            self._loop_started = True

    def loop_stop(self) -> None:
        if self._loop_started:
            self._client.loop_stop()
            self._loop_started = False

    def start(self) -> "HandballStreamClient":
        self.connect()
        self.loop_start()
        return self

    def stop(self) -> None:
        self.loop_stop()
        self.disconnect()

    def subscribe(self, topics: Sequence[str], *, qos: int = 0) -> list[str]:
        subscribed: list[str] = []
        for topic in topics:
            self._client.subscribe(topic, qos=qos)
            subscribed.append(topic)
        return subscribed

    def subscribe_granted_topics(self, *, qos: int = 0) -> list[str]:
        topics = self.access_grant.read_topics(
            include_catchup=self.include_catchup,
            include_response=self.include_response,
        )
        return self.subscribe(topics, qos=qos)

    def publish(
        self,
        topic: str,
        payload: bytes | str | dict[str, object] | list[object],
        *,
        qos: int = 0,
        retain: bool = False,
    ) -> StreamPublishResult:
        message_payload: bytes | str
        if isinstance(payload, dict | list):
            message_payload = json.dumps(payload)
        else:
            message_payload = payload

        info = self._client.publish(
            topic,
            payload=message_payload,
            qos=qos,
            retain=retain,
        )
        mid = getattr(info, "mid", None)
        rc = getattr(info, "rc", None)
        return StreamPublishResult(mid=mid, rc=rc)

    def publish_to_scope(
        self,
        scope: str,
        payload: bytes | str | dict[str, object] | list[object],
        *,
        qos: int = 0,
        retain: bool = False,
        permission: str = "write",
    ) -> StreamPublishResult:
        topic = self.access_grant.topic_for_scope(scope, permission=permission)
        return self.publish(topic, payload, qos=qos, retain=retain)

    def set_on_message(self, handler: StreamMessageHandler | None) -> None:
        self._on_message_handler = handler

    def set_on_connect(self, handler: StreamConnectHandler | None) -> None:
        self._on_connect_handler = handler

    def set_on_disconnect(self, handler: StreamDisconnectHandler | None) -> None:
        self._on_disconnect_handler = handler

    def _handle_connect(
        self,
        client: object,
        userdata: object,
        flags: object,
        reason_code: object,
        properties: object = None,
    ) -> None:
        del client, userdata, flags, reason_code, properties
        if self.auto_subscribe:
            self.subscribe_granted_topics()
        if self._on_connect_handler is not None:
            self._on_connect_handler()

    def _handle_disconnect(
        self,
        client: object,
        userdata: object,
        disconnect_flags: object,
        reason_code: object,
        properties: object = None,
    ) -> None:
        del client, userdata, disconnect_flags, properties
        if self._on_disconnect_handler is not None:
            self._on_disconnect_handler(
                int(reason_code) if isinstance(reason_code, int) else 0
            )

    def _handle_message(
        self,
        client: object,
        userdata: object,
        message: object,
    ) -> None:
        del client, userdata
        topic = getattr(message, "topic", None)
        payload = getattr(message, "payload", None)
        if not isinstance(topic, str) or not isinstance(payload, bytes):
            raise UnexpectedResponseError("Invalid MQTT message received.")

        decoded_message = decode_stream_message(topic, payload)
        if self._on_message_handler is not None:
            self._on_message_handler(decoded_message)

    def __enter__(self) -> "HandballStreamClient":
        return self.start()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        del exc_type, exc, traceback
        self.stop()


class HandballStreamingAPI:
    """Separate access client for the DataCore streaming API."""

    def __init__(  # noqa: PLR0913
        self,
        *,
        client_id: str,
        client_secret: str,
        sport: str,
        token_base_url: str | None = None,
        auth_url: str | None = None,
        timeout: int = 5,
        session: httpx.Client | None = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.sport = sport
        self.timeout = timeout

        self.token_base_url = self._resolve_token_base_url(
            token_base_url=token_base_url,
            auth_url=auth_url,
        )

        self.session = session or httpx.Client(
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        self._owns_session = session is None

    @staticmethod
    def _resolve_token_base_url(
        *, token_base_url: str | None, auth_url: str | None
    ) -> str:
        if token_base_url:
            return token_base_url.rstrip("/")
        if not auth_url:
            raise ValidationError("token_base_url or auth_url must be provided.")

        normalized_auth_url = auth_url.rstrip("/")
        suffix = "/oauth2/rest/token"
        if normalized_auth_url.endswith(suffix):
            return normalized_auth_url.removesuffix(suffix)
        return normalized_auth_url

    def _post_stream_access(
        self,
        path: str,
        payload: dict[str, object],
    ) -> StreamAccessGrant:
        url = f"{self.token_base_url}{path}"
        try:
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TransportError(f"Streaming access request failed: {exc}") from exc

        try:
            body = response.json()
        except ValueError as exc:
            raise UnexpectedResponseError(
                "Streaming access response is not valid JSON."
            ) from exc

        data = body.get("data")
        if not isinstance(data, dict):
            raise UnexpectedResponseError("Streaming access response is missing data.")

        url_value = data.get("url")
        client_id_value = data.get("clientId")
        topics_value = data.get("topics", [])

        if not isinstance(url_value, str) or not isinstance(client_id_value, str):
            raise UnexpectedResponseError(
                "Streaming access response is missing url or clientId."
            )
        if not isinstance(topics_value, list):
            raise UnexpectedResponseError(
                "Streaming access response topics field must be a list."
            )

        topics: list[StreamTopicGrant] = []
        for topic_entry in topics_value:
            if not isinstance(topic_entry, dict):
                raise UnexpectedResponseError(
                    "Streaming access response contains an invalid topic entry."
                )

            topic_name = topic_entry.get("topic")
            scope = topic_entry.get("scope")
            permission = topic_entry.get("permission")
            if (
                not isinstance(topic_name, str)
                or not isinstance(scope, str)
                or not isinstance(permission, str)
            ):
                raise UnexpectedResponseError(
                    "Streaming access response contains an incomplete topic entry."
                )

            topics.append(
                StreamTopicGrant(
                    topic=topic_name,
                    scope=scope,
                    permission=permission,
                )
            )

        return StreamAccessGrant(
            url=url_value,
            client_id=client_id_value,
            topics=tuple(topics),
        )

    def get_fixture_access(
        self,
        fixture_id: str,
        scopes: Sequence[str],
        *,
        include_port: bool = False,
    ) -> StreamAccessGrant:
        if not fixture_id:
            raise ValidationError("fixture_id must be provided.")
        if not scopes:
            raise ValidationError("At least one stream scope must be provided.")

        payload: dict[str, object] = {
            "credentialId": self.client_id,
            "credentialSecret": self.client_secret,
            "fixtureId": fixture_id,
            "sport": self.sport,
            "scopes": list(scopes),
            "includePort": include_port,
        }
        return self._post_stream_access("/stream/fixture/access", payload)

    def get_venue_access(
        self,
        venue_id: str,
        scopes: Sequence[str],
        *,
        include_port: bool = False,
    ) -> StreamAccessGrant:
        if not venue_id:
            raise ValidationError("venue_id must be provided.")
        if not scopes:
            raise ValidationError("At least one stream scope must be provided.")

        payload: dict[str, object] = {
            "credentialId": self.client_id,
            "credentialSecret": self.client_secret,
            "venueId": venue_id,
            "sport": self.sport,
            "scopes": list(scopes),
            "includePort": include_port,
        }
        return self._post_stream_access("/stream/venue/access", payload)

    def get_specific_fixture_access(
        self,
        topics: Sequence[str],
        scopes: Sequence[str],
    ) -> StreamAccessGrant:
        if not topics:
            raise ValidationError("At least one topic must be provided.")
        if not scopes:
            raise ValidationError("At least one stream scope must be provided.")

        payload: dict[str, object] = {
            "credentialId": self.client_id,
            "credentialSecret": self.client_secret,
            "topics": list(topics),
            "scopes": list(scopes),
        }
        return self._post_stream_access("/stream/fixture/specific", payload)

    def create_fixture_stream(  # noqa: PLR0913
        self,
        fixture_id: str,
        scopes: Sequence[str],
        *,
        include_port: bool = False,
        keepalive: int = 15,
        auto_subscribe: bool = True,
        include_catchup: bool = True,
        include_response: bool = True,
        on_message: StreamMessageHandler | None = None,
        on_connect: StreamConnectHandler | None = None,
        on_disconnect: StreamDisconnectHandler | None = None,
    ) -> HandballStreamClient:
        access_grant = self.get_fixture_access(
            fixture_id,
            scopes,
            include_port=include_port,
        )
        return HandballStreamClient(
            access_grant,
            keepalive=keepalive,
            auto_subscribe=auto_subscribe,
            include_catchup=include_catchup,
            include_response=include_response,
            on_message=on_message,
            on_connect=on_connect,
            on_disconnect=on_disconnect,
        )

    def create_venue_stream(  # noqa: PLR0913
        self,
        venue_id: str,
        scopes: Sequence[str],
        *,
        include_port: bool = False,
        keepalive: int = 15,
        auto_subscribe: bool = True,
        include_catchup: bool = True,
        include_response: bool = True,
        on_message: StreamMessageHandler | None = None,
        on_connect: StreamConnectHandler | None = None,
        on_disconnect: StreamDisconnectHandler | None = None,
    ) -> HandballStreamClient:
        access_grant = self.get_venue_access(
            venue_id,
            scopes,
            include_port=include_port,
        )
        return HandballStreamClient(
            access_grant,
            keepalive=keepalive,
            auto_subscribe=auto_subscribe,
            include_catchup=include_catchup,
            include_response=include_response,
            on_message=on_message,
            on_connect=on_connect,
            on_disconnect=on_disconnect,
        )

    def close(self) -> None:
        if self._owns_session:
            self.session.close()

    def __enter__(self) -> "HandballStreamingAPI":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        del exc_type, exc, traceback
        self.close()
