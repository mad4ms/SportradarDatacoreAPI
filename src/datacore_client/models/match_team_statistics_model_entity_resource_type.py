from enum import Enum


class MatchTeamStatisticsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
