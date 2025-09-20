from enum import Enum


class StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingGrouping(
    str, Enum
):
    NONE = "NONE"
    STAGE = "STAGE"
    STAGEPOOL = "STAGEPOOL"

    def __str__(self) -> str:
        return str(self.value)
