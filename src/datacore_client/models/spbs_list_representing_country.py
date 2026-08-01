from enum import Enum


class SpbsListRepresentingCountry(str, Enum):
    ANY = "ANY"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
