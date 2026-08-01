from enum import Enum


class GameLogPersonModelPositionType2Type1(str, Enum):
    CB = "CB"
    D = "D"
    G = "G"
    LB = "LB"
    LW = "LW"
    P = "P"
    RB = "RB"
    RW = "RW"

    def __str__(self) -> str:
        return str(self.value)
