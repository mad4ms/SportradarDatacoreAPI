from enum import Enum


class FixtureByCompetitionListDiscipline(str, Enum):
    BEACH = "BEACH"
    HOCKEY5S = "HOCKEY5S"
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"
    PARAHOCKEY = "PARAHOCKEY"

    def __str__(self) -> str:
        return str(self.value)
