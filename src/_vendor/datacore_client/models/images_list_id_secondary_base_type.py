from enum import Enum


class ImagesListIdSecondaryBaseType(str, Enum):
    COMPETITION = "COMPETITION"
    CONFERENCE = "CONFERENCE"
    DIVISION = "DIVISION"
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    LEAGUE = "LEAGUE"
    ORGANIZATION = "ORGANIZATION"
    PERSON = "PERSON"
    SEASON = "SEASON"
    UNIFORM = "UNIFORM"
    UNIFORM_ITEM = "UNIFORM_ITEM"

    def __str__(self) -> str:
        return str(self.value)
