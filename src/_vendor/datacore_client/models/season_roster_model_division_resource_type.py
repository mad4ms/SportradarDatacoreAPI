from enum import Enum


class SeasonRosterModelDivisionResourceType(str, Enum):
    DIVISIONS = "divisions"

    def __str__(self) -> str:
        return str(self.value)
