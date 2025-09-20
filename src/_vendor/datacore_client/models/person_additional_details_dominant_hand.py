from enum import Enum


class PersonAdditionalDetailsDominantHand(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
