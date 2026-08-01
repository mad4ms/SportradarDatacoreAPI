from enum import Enum


class MatchPersonStatisticsPeriodsModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
