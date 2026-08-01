from enum import Enum


class SeasonPersonBaseStatisticsModelSeasonResourceType(str, Enum):
    SEASONS = "seasons"

    def __str__(self) -> str:
        return str(self.value)
