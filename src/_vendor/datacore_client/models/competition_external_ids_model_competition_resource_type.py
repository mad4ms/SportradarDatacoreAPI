from enum import Enum


class CompetitionExternalIdsModelCompetitionResourceType(str, Enum):
    COMPETITIONS = "competitions"

    def __str__(self) -> str:
        return str(self.value)
