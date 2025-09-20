from enum import Enum


class MatchTeamsModelUniformResourceType(str, Enum):
    UNIFORMS = "uniforms"

    def __str__(self) -> str:
        return str(self.value)
