from enum import Enum


class CompetitionListSeasonStatusSeasonVideoProduction(str, Enum):
    AUTOMATED = "AUTOMATED"
    MANUAL = "MANUAL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
