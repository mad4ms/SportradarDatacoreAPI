from enum import Enum


class SeasonPersonBaseStatisticsModelCompetitorType(str, Enum):
    ENTITY = "ENTITY"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
