from enum import Enum


class StandingListGroupingConferenceDivision(str, Enum):
    CONFERENCE = "CONFERENCE"
    DIVISION = "DIVISION"
    OVERALL = "OVERALL"

    def __str__(self) -> str:
        return str(self.value)
