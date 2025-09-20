from enum import Enum


class SeasonInsertSeasonPostBodyRepresentation(str, Enum):
    CLUB = "CLUB"
    COUNTRY = "COUNTRY"
    PERSON = "PERSON"
    REGION = "REGION"
    STATE = "STATE"

    def __str__(self) -> str:
        return str(self.value)
