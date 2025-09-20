from enum import Enum


class MatchModelStageResourceType(str, Enum):
    SEASONSTAGES = "seasonStages"

    def __str__(self) -> str:
        return str(self.value)
