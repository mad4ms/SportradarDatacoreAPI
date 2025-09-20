from enum import Enum


class EntityUpdateTeamPutBodyAgeGroupType3Type1(str, Enum):
    JUNIOR = "JUNIOR"
    MASTERS = "MASTERS"
    SENIOR = "SENIOR"
    UNDER_10 = "UNDER_10"
    UNDER_11 = "UNDER_11"
    UNDER_12 = "UNDER_12"
    UNDER_13 = "UNDER_13"
    UNDER_14 = "UNDER_14"
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
