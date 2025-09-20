from enum import Enum


class TransfersInsertTransferPostBodyTransferType(str, Enum):
    DROPPED = "DROPPED"
    OTHER = "OTHER"
    PERMIT = "PERMIT"
    TRADE = "TRADE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
