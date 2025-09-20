from enum import Enum


class SeasonEntitiesModelConferenceResourceType(str, Enum):
    CONFERENCES = "conferences"

    def __str__(self) -> str:
        return str(self.value)
