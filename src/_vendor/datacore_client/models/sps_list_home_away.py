from enum import Enum


class SpsListHomeAway(str, Enum):
    AWAY = "AWAY"
    HOME = "HOME"

    def __str__(self) -> str:
        return str(self.value)
