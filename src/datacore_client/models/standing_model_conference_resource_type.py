from enum import Enum


class StandingModelConferenceResourceType(str, Enum):
    CONFERENCES = "conferences"

    def __str__(self) -> str:
        return str(self.value)
