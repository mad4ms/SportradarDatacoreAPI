from enum import Enum


class SeasonRosterDetailStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INJURED = "INJURED"
    OTHER_NOT_PARTICIPATING = "OTHER_NOT_PARTICIPATING"
    OUT = "OUT"
    SUSPENSED = "SUSPENSED"

    def __str__(self) -> str:
        return str(self.value)
