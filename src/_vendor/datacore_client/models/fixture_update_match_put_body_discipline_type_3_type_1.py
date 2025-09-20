from enum import Enum


class FixtureUpdateMatchPutBodyDisciplineType3Type1(str, Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"

    def __str__(self) -> str:
        return str(self.value)
