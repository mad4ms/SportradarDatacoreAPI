from enum import Enum


class SeasonModelSeasonType(str, Enum):
    MULTI_YEAR_HISTORICAL = "MULTI_YEAR_HISTORICAL"
    ONE_OFF = "ONE_OFF"
    PRESEASON = "PRESEASON"
    SEASON = "SEASON"
    TOURNAMENT = "TOURNAMENT"

    def __str__(self) -> str:
        return str(self.value)
