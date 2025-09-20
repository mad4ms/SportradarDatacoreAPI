from enum import Enum


class LeaderQualifierModelLeadersCriteriaResourceType(str, Enum):
    LEADERCRITERIA = "leaderCriteria"

    def __str__(self) -> str:
        return str(self.value)
