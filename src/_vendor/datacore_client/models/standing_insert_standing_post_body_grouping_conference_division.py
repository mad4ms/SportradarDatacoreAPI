from enum import Enum


class StandingInsertStandingPostBodyGroupingConferenceDivision(str, Enum):
    CONFERENCE = "CONFERENCE"
    DIVISION = "DIVISION"
    OVERALL = "OVERALL"

    def __str__(self) -> str:
        return str(self.value)
