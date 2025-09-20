from enum import Enum


class StandingAdjustmentModelDivisionResourceType(str, Enum):
    DIVISIONS = "divisions"

    def __str__(self) -> str:
        return str(self.value)
