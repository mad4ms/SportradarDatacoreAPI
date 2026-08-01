from enum import Enum


class StandingModelStandingConfigurationResourceType(str, Enum):
    STANDINGCONFIGURATIONS = "standingConfigurations"

    def __str__(self) -> str:
        return str(self.value)
