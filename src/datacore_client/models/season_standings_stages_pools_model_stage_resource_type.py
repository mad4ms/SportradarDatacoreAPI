from enum import Enum


class SeasonStandingsStagesPoolsModelStageResourceType(str, Enum):
    SEASONSTAGES = "seasonStages"

    def __str__(self) -> str:
        return str(self.value)
