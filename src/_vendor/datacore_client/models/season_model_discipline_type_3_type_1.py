from enum import Enum


class SeasonModelDisciplineType3Type1(str, Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"

    def __str__(self) -> str:
        return str(self.value)
