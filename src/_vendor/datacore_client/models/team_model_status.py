from enum import Enum


class TeamModelStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
