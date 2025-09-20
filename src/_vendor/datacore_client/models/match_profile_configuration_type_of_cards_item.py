from enum import Enum


class MatchProfileConfigurationTypeOfCardsItem(str, Enum):
    BLUE = "Blue"
    RED = "Red"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
