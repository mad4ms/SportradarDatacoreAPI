from enum import Enum


class SeasonInsertSeasonPostBodyEventType(str, Enum):
    FIXTURE = "FIXTURE"
    PRACTICE = "PRACTICE"

    def __str__(self) -> str:
        return str(self.value)
