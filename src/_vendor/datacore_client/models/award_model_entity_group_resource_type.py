from enum import Enum


class AwardModelEntityGroupResourceType(str, Enum):
    ENTITYGROUPS = "entityGroups"

    def __str__(self) -> str:
        return str(self.value)
