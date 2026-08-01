from enum import Enum


class SeriesModelSeasonResourceType(str, Enum):
    SEASONS = "seasons"

    def __str__(self) -> str:
        return str(self.value)
