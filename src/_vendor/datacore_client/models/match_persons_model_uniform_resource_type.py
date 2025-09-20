from enum import Enum


class MatchPersonsModelUniformResourceType(str, Enum):
    UNIFORMS = "uniforms"

    def __str__(self) -> str:
        return str(self.value)
