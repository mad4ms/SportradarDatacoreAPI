from enum import Enum


class SeasonFixtureStagesPoolsModelSeasonResourceType(str, Enum):
    SEASONS = "seasons"

    def __str__(self) -> str:
        return str(self.value)
