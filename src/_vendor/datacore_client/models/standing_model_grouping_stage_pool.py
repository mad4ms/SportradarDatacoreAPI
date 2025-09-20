from enum import Enum


class StandingModelGroupingStagePool(str, Enum):
    OVERALL = "OVERALL"
    STAGE = "STAGE"
    STAGEPOOL = "STAGEPOOL"

    def __str__(self) -> str:
        return str(self.value)
