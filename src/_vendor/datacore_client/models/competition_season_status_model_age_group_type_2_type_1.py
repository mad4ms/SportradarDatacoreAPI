from enum import Enum


class CompetitionSeasonStatusModelAgeGroupType2Type1(str, Enum):
    JUNIOR = "JUNIOR"
    MASTERS = "MASTERS"
    SENIOR = "SENIOR"
    UNDER_15 = "UNDER_15"
    UNDER_16 = "UNDER_16"
    UNDER_17 = "UNDER_17"
    UNDER_18 = "UNDER_18"
    UNDER_19 = "UNDER_19"
    UNDER_20 = "UNDER_20"
    UNDER_21 = "UNDER_21"
    UNDER_22 = "UNDER_22"
    UNDER_23 = "UNDER_23"
    YOUTH = "YOUTH"

    def __str__(self) -> str:
        return str(self.value)
