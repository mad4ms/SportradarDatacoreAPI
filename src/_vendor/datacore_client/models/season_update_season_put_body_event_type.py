from enum import Enum


class SeasonUpdateSeasonPutBodyEventType(str, Enum):
    FIXTURE = "FIXTURE"
    PRACTICE = "PRACTICE"

    def __str__(self) -> str:
        return str(self.value)
