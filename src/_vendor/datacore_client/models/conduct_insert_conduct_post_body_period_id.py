from enum import IntEnum


class ConductInsertConductPostBodyPeriodId(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14

    def __str__(self) -> str:
        return str(self.value)
