from enum import Enum


class MatchTeamPeriodStatisticsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
