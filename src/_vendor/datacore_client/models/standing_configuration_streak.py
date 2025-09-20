from enum import Enum


class StandingConfigurationStreak(str, Enum):
    NONLOST = "NONLOST"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
