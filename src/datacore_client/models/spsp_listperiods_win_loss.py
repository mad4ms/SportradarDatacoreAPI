from enum import Enum


class SpspListperiodsWinLoss(str, Enum):
    DRAW = "DRAW"
    LOSS = "LOSS"
    WIN = "WIN"

    def __str__(self) -> str:
        return str(self.value)
