from enum import Enum


class EntityUpdateTeamPutBodyGenderType2Type1(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    MIXED = "MIXED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
