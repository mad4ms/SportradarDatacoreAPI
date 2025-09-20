from enum import Enum


class CaprsListHomeAway(str, Enum):
    AWAY = "AWAY"
    HOME = "HOME"

    def __str__(self) -> str:
        return str(self.value)
