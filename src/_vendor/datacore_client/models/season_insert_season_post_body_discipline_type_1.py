from enum import Enum


class SeasonInsertSeasonPostBodyDisciplineType1(str, Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"

    def __str__(self) -> str:
        return str(self.value)
