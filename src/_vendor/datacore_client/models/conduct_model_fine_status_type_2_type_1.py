from enum import Enum


class ConductModelFineStatusType2Type1(str, Enum):
    CANCELLED = "CANCELLED"
    ISSUED = "ISSUED"
    OTHER = "OTHER"
    PAID = "PAID"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
