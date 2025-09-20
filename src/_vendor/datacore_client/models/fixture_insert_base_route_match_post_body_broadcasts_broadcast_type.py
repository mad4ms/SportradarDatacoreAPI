from enum import Enum


class FixtureInsertBaseRouteMatchPostBodyBroadcastsBroadcastType(str, Enum):
    PAY_PER_VIEW = "PAY_PER_VIEW"
    RADIO = "RADIO"
    STREAMING_AUDIO = "STREAMING_AUDIO"
    STREAMING_VIDEO = "STREAMING_VIDEO"
    TV = "TV"

    def __str__(self) -> str:
        return str(self.value)
