from enum import Enum


class SeasonSeriesCompetitorSeriesResult(str, Enum):
    DRAW = "DRAW"
    LOST = "LOST"
    PENDING = "PENDING"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
