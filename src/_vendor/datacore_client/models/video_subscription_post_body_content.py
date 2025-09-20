from enum import Enum


class VideoSubscriptionPostBodyContent(str, Enum):
    CLEAN = "CLEAN"
    PROGRAM = "PROGRAM"

    def __str__(self) -> str:
        return str(self.value)
