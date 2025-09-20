from enum import Enum


class UniformsUpdateUniformsPutBodyBaseType(str, Enum):
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
