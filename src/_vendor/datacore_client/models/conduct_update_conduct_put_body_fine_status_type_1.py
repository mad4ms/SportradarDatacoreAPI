from enum import Enum


class ConductUpdateConductPutBodyFineStatusType1(str, Enum):
    CANCELLED = "CANCELLED"
    ISSUED = "ISSUED"
    OTHER = "OTHER"
    PAID = "PAID"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
