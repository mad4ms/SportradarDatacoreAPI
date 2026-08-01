from enum import Enum


class StandingAdjustmentModelRoundResourceType(str, Enum):
    SEASONROUNDS = "seasonRounds"

    def __str__(self) -> str:
        return str(self.value)
