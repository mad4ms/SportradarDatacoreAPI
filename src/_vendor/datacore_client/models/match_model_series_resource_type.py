from enum import Enum


class MatchModelSeriesResourceType(str, Enum):
    SEASONSERIES = "seasonSeries"

    def __str__(self) -> str:
        return str(self.value)
