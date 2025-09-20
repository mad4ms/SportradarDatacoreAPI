from enum import Enum


class LeaderQualifierModelComparisonType(str, Enum):
    EQUAL = "EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_EQUAL = "LESS_THAN_EQUAL"

    def __str__(self) -> str:
        return str(self.value)
