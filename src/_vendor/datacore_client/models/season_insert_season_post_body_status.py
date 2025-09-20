from enum import Enum


class SeasonInsertSeasonPostBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETE = "COMPLETE"
    DRAFT = "DRAFT"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
