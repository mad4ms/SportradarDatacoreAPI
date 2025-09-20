from enum import Enum


class MatchPersonStatisticsPeriodsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
