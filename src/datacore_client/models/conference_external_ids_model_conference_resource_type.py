from enum import Enum


class ConferenceExternalIdsModelConferenceResourceType(str, Enum):
    CONFERENCES = "conferences"

    def __str__(self) -> str:
        return str(self.value)
