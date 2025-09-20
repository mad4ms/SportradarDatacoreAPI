from enum import Enum


class StandingPutBodyGroupingBase(str, Enum):
    OVERALL = "OVERALL"
    ROUND = "ROUND"

    def __str__(self) -> str:
        return str(self.value)
