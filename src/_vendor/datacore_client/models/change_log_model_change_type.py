from enum import Enum


class ChangeLogModelChangeType(str, Enum):
    DELETE = "delete"
    FIXTURE_CHANGE = "fixture_change"
    FIXTURE_RESET = "fixture_reset"
    FIXTURE_VIDEOSTREAM_DISABLE = "fixture_videostream_disable"
    FIXTURE_VIDEOSTREAM_ENABLE = "fixture_videostream_enable"
    MOVE = "move"
    POST = "post"
    PUT = "put"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
