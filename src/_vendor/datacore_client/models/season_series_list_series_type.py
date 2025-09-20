from enum import Enum


class SeasonSeriesListSeriesType(str, Enum):
    BEST_OF = "BEST_OF"
    HEAD_TO_HEAD = "HEAD_TO_HEAD"
    HOME_AND_AWAY = "HOME_AND_AWAY"
    KNOCKOUT = "KNOCKOUT"
    TOURNAMENT = "TOURNAMENT"

    def __str__(self) -> str:
        return str(self.value)
