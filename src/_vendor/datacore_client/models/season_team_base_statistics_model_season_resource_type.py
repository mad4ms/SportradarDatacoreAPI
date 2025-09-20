from enum import Enum


class SeasonTeamBaseStatisticsModelSeasonResourceType(str, Enum):
    SEASONS = "seasons"

    def __str__(self) -> str:
        return str(self.value)
