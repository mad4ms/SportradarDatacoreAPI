from enum import Enum


class SebsListRepresentingCountry(str, Enum):
    ANY = "ANY"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
