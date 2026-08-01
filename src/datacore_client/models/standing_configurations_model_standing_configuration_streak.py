from enum import Enum


class StandingConfigurationsModelStandingConfigurationStreak(str, Enum):
    NONLOST = "NONLOST"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
