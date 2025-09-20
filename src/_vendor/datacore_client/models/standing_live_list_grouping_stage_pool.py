from enum import Enum


class StandingLiveListGroupingStagePool(str, Enum):
    OVERALL = "OVERALL"
    STAGE = "STAGE"
    STAGEPOOL = "STAGEPOOL"

    def __str__(self) -> str:
        return str(self.value)
