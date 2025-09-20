from enum import Enum


class MatchPersonsModelEntityGroupResourceType(str, Enum):
    ENTITYGROUPS = "entityGroups"

    def __str__(self) -> str:
        return str(self.value)
