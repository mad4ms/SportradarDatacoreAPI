from enum import Enum


class SeasonStandingsStagesPoolsModelSeasonResourceType(str, Enum):
    SEASONS = "seasons"

    def __str__(self) -> str:
        return str(self.value)
