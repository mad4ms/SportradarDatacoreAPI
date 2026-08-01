from enum import Enum


class UniformItemsModelUniformResourceType(str, Enum):
    UNIFORMS = "uniforms"

    def __str__(self) -> str:
        return str(self.value)
