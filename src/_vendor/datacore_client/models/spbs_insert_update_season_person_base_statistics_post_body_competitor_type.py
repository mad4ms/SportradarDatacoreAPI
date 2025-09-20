from enum import Enum


class SpbsInsertUpdateSeasonPersonBaseStatisticsPostBodyCompetitorType(str, Enum):
    ENTITY = "ENTITY"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
