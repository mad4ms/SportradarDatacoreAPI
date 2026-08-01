from enum import Enum


class SeasonListVideoProduction(str, Enum):
    AUTOMATED = "AUTOMATED"
    MANUAL = "MANUAL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
