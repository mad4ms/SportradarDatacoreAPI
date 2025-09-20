from enum import Enum


class SeasonTeamsModelRosterStatus(str, Enum):
    APPROVED = "APPROVED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
