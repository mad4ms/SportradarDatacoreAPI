from enum import Enum


class StandingAdjustmentPutBodyAdjustmentType(str, Enum):
    ADD_MINUS = "ADD_MINUS"
    SET = "SET"

    def __str__(self) -> str:
        return str(self.value)
