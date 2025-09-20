from enum import Enum


class CaprsListRepresentingCountry(str, Enum):
    ANY = "ANY"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
