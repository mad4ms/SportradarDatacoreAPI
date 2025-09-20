from enum import Enum


class StandingAdjustmentsUpdateStandingAdjustmentPutBodyAdjustmentType(str, Enum):
    ADD_MINUS = "ADD_MINUS"
    SET = "SET"

    def __str__(self) -> str:
        return str(self.value)
