from enum import Enum


class VideoStreamInputsModelCompetitionResourceType(str, Enum):
    COMPETITIONS = "competitions"

    def __str__(self) -> str:
        return str(self.value)
