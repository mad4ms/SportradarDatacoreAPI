from enum import Enum


class SeasonPersonStatisticsModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
