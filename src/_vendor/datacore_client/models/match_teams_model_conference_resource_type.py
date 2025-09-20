from enum import Enum


class MatchTeamsModelConferenceResourceType(str, Enum):
    CONFERENCES = "conferences"

    def __str__(self) -> str:
        return str(self.value)
