from enum import Enum


class SeasonModelStandingConfigurationResourceType(str, Enum):
    STANDINGCONFIGURATIONS = "standingConfigurations"

    def __str__(self) -> str:
        return str(self.value)
