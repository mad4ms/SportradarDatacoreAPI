from enum import Enum


class GamelogListpersonHomeAway(str, Enum):
    AWAY = "AWAY"
    HOME = "HOME"

    def __str__(self) -> str:
        return str(self.value)
