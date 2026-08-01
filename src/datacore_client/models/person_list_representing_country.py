from enum import Enum


class PersonListRepresentingCountry(str, Enum):
    ANY = "ANY"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
