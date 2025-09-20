from enum import Enum


class StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionForExtraDepthH2HsSortDirection(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
