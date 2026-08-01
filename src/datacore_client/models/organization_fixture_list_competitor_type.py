from enum import Enum


class OrganizationFixtureListCompetitorType(str, Enum):
    ENTITY = "ENTITY"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
