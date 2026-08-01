from enum import Enum


class SesListHomeAway(str, Enum):
    AWAY = "AWAY"
    HOME = "HOME"

    def __str__(self) -> str:
        return str(self.value)
