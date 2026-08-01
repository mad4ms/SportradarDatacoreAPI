from enum import Enum


class GameLogPersonModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
