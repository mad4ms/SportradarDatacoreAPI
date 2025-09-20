from enum import Enum


class SeasonSeriesInsertSeriesPostBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETE = "COMPLETE"
    NOT_STARTED = "NOT_STARTED"

    def __str__(self) -> str:
        return str(self.value)
