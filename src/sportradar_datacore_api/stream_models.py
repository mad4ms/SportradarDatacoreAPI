"""Typed models used by the DataCore streaming API."""

from dataclasses import dataclass

from sportradar_datacore_api.errors import NotFoundError


@dataclass(frozen=True, slots=True)
class StreamTopicGrant:
    """A single topic permission returned by the streaming access API."""

    topic: str
    scope: str
    permission: str

    @property
    def is_read(self) -> bool:
        return self.permission == "read"

    @property
    def is_write(self) -> bool:
        return self.permission == "write"

    @property
    def is_catchup(self) -> bool:
        return "catchup" in self.scope.casefold()

    @property
    def is_response(self) -> bool:
        return self.scope == "read:response" or self.topic.endswith("/response")


@dataclass(frozen=True, slots=True)
class StreamAccessGrant:
    """Connection details for a streaming session."""

    url: str
    client_id: str
    topics: tuple[StreamTopicGrant, ...]

    def read_topics(
        self,
        *,
        include_catchup: bool = True,
        include_response: bool = True,
    ) -> list[str]:
        selected: list[str] = []
        for topic in self.topics:
            if not topic.is_read:
                continue
            if not include_catchup and topic.is_catchup:
                continue
            if not include_response and topic.is_response:
                continue
            selected.append(topic.topic)
        return selected

    def write_topics(self) -> list[str]:
        return [topic.topic for topic in self.topics if topic.is_write]

    def topic_for_scope(self, scope: str, *, permission: str | None = None) -> str:
        for topic in self.topics:
            if topic.scope != scope:
                continue
            if permission is not None and topic.permission != permission:
                continue
            return topic.topic
        raise NotFoundError(f"No topic grant found for scope '{scope}'.")


@dataclass(frozen=True, slots=True)
class StreamMessage:
    """A decoded MQTT message from the streaming API."""

    topic: str
    raw_payload: bytes
    payload: object
    message_type: str | None
    decoded_compressed_data: object | None = None


@dataclass(frozen=True, slots=True)
class StreamPublishResult:
    """Result returned by MQTT publish operations."""

    mid: int | None
    rc: int | None
