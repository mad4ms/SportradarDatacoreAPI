from enum import Enum


class MatchProfilesModelMatchProfileConfigurationTypeOfCardsItem(str, Enum):
    BLUE = "Blue"
    RED = "Red"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
