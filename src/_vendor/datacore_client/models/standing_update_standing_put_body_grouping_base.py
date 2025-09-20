from enum import Enum


class StandingUpdateStandingPutBodyGroupingBase(str, Enum):
    OVERALL = "OVERALL"
    ROUND = "ROUND"

    def __str__(self) -> str:
        return str(self.value)
