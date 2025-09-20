from enum import Enum


class StandingAdjustmentsInsertStandingAdjustmentPostBodyAdjustmentType(str, Enum):
    ADD_MINUS = "ADD_MINUS"
    SET = "SET"

    def __str__(self) -> str:
        return str(self.value)
