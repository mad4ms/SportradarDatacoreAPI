from enum import Enum


class CareerPersonRepresentationalStatisticsModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
