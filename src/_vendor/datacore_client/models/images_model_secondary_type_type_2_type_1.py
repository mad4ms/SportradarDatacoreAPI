from enum import Enum


class ImagesModelSecondaryTypeType2Type1(str, Enum):
    COMPETITION = "COMPETITION"
    CONFERENCE = "CONFERENCE"
    DIVISION = "DIVISION"
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    LEAGUE = "LEAGUE"
    SEASON = "SEASON"

    def __str__(self) -> str:
        return str(self.value)
