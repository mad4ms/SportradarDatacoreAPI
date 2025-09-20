from enum import Enum


class MatchTeamsModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
