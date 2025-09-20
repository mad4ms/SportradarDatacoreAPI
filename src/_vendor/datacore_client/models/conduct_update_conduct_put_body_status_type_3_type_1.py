from enum import Enum


class ConductUpdateConductPutBodyStatusType3Type1(str, Enum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    COMPLETE = "COMPLETE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
