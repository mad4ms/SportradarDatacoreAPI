from enum import Enum


class SeasonTeamsModelConferenceResourceType(str, Enum):
    CONFERENCES = "conferences"

    def __str__(self) -> str:
        return str(self.value)
