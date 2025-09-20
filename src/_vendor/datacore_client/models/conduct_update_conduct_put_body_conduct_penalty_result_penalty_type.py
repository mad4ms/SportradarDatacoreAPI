from enum import Enum


class ConductUpdateConductPutBodyConductPenaltyResultPenaltyType(str, Enum):
    FINANCIAL = "FINANCIAL"
    GAMES = "GAMES"
    MONTHS = "MONTHS"
    WEEKS = "WEEKS"
    YEARS = "YEARS"

    def __str__(self) -> str:
        return str(self.value)
