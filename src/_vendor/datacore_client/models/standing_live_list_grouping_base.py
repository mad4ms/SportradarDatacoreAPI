from enum import Enum


class StandingLiveListGroupingBase(str, Enum):
    OVERALL = "OVERALL"
    ROUND = "ROUND"

    def __str__(self) -> str:
        return str(self.value)
