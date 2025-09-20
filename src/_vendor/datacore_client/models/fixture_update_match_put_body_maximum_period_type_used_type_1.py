from enum import Enum


class FixtureUpdateMatchPutBodyMaximumPeriodTypeUsedType1(str, Enum):
    EXTRA_TIME = "EXTRA_TIME"
    OVERTIME = "OVERTIME"
    REGULAR = "REGULAR"
    SHOOTOUT = "SHOOTOUT"

    def __str__(self) -> str:
        return str(self.value)
