from enum import Enum


class EntityInsertTeamPostBodyDisciplineType1(str, Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"

    def __str__(self) -> str:
        return str(self.value)
