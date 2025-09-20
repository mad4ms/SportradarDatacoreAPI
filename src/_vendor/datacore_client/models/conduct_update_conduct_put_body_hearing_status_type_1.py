from enum import Enum


class ConductUpdateConductPutBodyHearingStatusType1(str, Enum):
    FINALIZED = "FINALIZED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
