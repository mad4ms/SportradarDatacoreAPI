from enum import Enum


class SeasonSeriesUpdateSeriesPutBodySeriesType(str, Enum):
    BEST_OF = "BEST_OF"
    HOME_AND_AWAY = "HOME_AND_AWAY"
    KNOCKOUT = "KNOCKOUT"

    def __str__(self) -> str:
        return str(self.value)
