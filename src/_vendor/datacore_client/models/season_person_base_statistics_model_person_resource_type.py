from enum import Enum


class SeasonPersonBaseStatisticsModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
