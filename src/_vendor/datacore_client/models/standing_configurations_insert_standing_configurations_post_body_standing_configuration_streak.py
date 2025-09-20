from enum import Enum


class StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfigurationStreak(
    str, Enum
):
    NONLOST = "NONLOST"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
