from enum import Enum


class FixtureInsertBaseRouteMatchPostBodyDisciplineType2Type1(str, Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"

    def __str__(self) -> str:
        return str(self.value)
