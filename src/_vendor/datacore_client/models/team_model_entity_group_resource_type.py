from enum import Enum


class TeamModelEntityGroupResourceType(str, Enum):
    ENTITYGROUPS = "entityGroups"

    def __str__(self) -> str:
        return str(self.value)
