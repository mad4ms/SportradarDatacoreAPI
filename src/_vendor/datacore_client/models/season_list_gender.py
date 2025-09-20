from enum import Enum


class SeasonListGender(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    MIXED = "MIXED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
