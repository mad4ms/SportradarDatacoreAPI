from enum import Enum


class CaprsListRepresentation(str, Enum):
    CLUB = "CLUB"
    COUNTRY = "COUNTRY"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
