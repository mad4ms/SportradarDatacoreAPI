from enum import Enum


class FixtureInsertBaseRouteMatchPostBodyCompetitorType(str, Enum):
    ENTITY = "ENTITY"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
