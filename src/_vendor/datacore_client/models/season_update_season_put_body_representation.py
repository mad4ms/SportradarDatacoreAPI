from enum import Enum


class SeasonUpdateSeasonPutBodyRepresentation(str, Enum):
    CLUB = "CLUB"
    COUNTRY = "COUNTRY"
    PERSON = "PERSON"
    REGION = "REGION"
    STATE = "STATE"

    def __str__(self) -> str:
        return str(self.value)
