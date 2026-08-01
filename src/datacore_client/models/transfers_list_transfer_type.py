from enum import Enum


class TransfersListTransferType(str, Enum):
    DROPPED = "DROPPED"
    OTHER = "OTHER"
    PERMIT = "PERMIT"
    TRADE = "TRADE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
