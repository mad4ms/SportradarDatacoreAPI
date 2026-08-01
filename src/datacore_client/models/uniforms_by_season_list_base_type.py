from enum import Enum


class UniformsBySeasonListBaseType(str, Enum):
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
