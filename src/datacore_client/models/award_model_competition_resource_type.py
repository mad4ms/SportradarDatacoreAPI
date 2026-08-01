from enum import Enum


class AwardModelCompetitionResourceType(str, Enum):
    COMPETITIONS = "competitions"

    def __str__(self) -> str:
        return str(self.value)
