from enum import Enum


class SeasonEntityStatisticsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
