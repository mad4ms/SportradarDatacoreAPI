from enum import Enum


class RoleModelPersonResourceType(str, Enum):
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
