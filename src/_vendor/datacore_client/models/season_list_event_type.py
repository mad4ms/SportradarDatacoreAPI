from enum import Enum


class SeasonListEventType(str, Enum):
    FIXTURE = "FIXTURE"
    PRACTICE = "PRACTICE"

    def __str__(self) -> str:
        return str(self.value)
