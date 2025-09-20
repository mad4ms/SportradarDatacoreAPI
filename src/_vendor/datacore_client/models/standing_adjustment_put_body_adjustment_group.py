from enum import Enum


class StandingAdjustmentPutBodyAdjustmentGroup(str, Enum):
    IN_CONFERENCE = "IN_CONFERENCE"
    IN_DIVISION = "IN_DIVISION"
    OUT_CONFERENCE = "OUT_CONFERENCE"
    OUT_DIVISION = "OUT_DIVISION"
    OVERALL = "OVERALL"

    def __str__(self) -> str:
        return str(self.value)
