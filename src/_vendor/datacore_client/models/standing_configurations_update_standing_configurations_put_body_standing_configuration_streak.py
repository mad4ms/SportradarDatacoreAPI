from enum import Enum


class StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak(
    str, Enum
):
    NONLOST = "NONLOST"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
