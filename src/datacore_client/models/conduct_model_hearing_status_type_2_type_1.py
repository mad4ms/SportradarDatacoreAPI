from enum import Enum


class ConductModelHearingStatusType2Type1(str, Enum):
    FINALIZED = "FINALIZED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
