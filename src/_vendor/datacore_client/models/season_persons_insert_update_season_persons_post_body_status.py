from enum import Enum


class SeasonPersonsInsertUpdateSeasonPersonsPostBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
