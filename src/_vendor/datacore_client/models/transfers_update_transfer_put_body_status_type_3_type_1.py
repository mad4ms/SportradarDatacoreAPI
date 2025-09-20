from enum import Enum


class TransfersUpdateTransferPutBodyStatusType3Type1(str, Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
