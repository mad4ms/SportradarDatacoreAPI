from enum import Enum


class ImagesListIdSecondarySecondaryType(str, Enum):
    COMPETITION = "COMPETITION"
    CONFERENCE = "CONFERENCE"
    DIVISION = "DIVISION"
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    LEAGUE = "LEAGUE"
    ORGANIZATION = "ORGANIZATION"
    SEASON = "SEASON"

    def __str__(self) -> str:
        return str(self.value)
