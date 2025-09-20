from enum import Enum


class UniformsInsertUniformsPostBodyBaseType(str, Enum):
    ENTITY = "ENTITY"
    ENTITYGROUP = "ENTITYGROUP"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
