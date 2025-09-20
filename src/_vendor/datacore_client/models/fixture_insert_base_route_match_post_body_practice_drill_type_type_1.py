from enum import Enum


class FixtureInsertBaseRouteMatchPostBodyPracticeDrillTypeType1(str, Enum):
    DRILL = "DRILL"
    FITNESS = "FITNESS"
    GAME = "GAME"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
