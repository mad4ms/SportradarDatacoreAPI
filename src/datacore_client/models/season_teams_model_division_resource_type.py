from enum import Enum


class SeasonTeamsModelDivisionResourceType(str, Enum):
    DIVISIONS = "divisions"

    def __str__(self) -> str:
        return str(self.value)
