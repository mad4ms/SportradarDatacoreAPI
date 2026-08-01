from enum import Enum


class SesListWinLoss(str, Enum):
    DRAW = "DRAW"
    LOSS = "LOSS"
    WIN = "WIN"

    def __str__(self) -> str:
        return str(self.value)
