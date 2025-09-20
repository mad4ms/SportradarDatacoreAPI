from enum import Enum


class FixtureProfilesUpdateMatchProfilesPutBodyMatchProfileConfigurationTypeOfCardsItem(
    str, Enum
):
    BLUE = "Blue"
    RED = "Red"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
