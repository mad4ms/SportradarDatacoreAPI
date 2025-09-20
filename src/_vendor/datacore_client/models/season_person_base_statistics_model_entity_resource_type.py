from enum import Enum


class SeasonPersonBaseStatisticsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
