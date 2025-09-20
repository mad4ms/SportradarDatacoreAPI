from enum import Enum


class StandingPutBodyFixtureType(str, Enum):
    ALL_STAR = "ALL_STAR"
    DEMONSTRATION = "DEMONSTRATION"
    FINAL = "FINAL"
    FRIENDLY = "FRIENDLY"
    PLAYOFF = "PLAYOFF"
    PRESEASON = "PRESEASON"
    REGULAR = "REGULAR"

    def __str__(self) -> str:
        return str(self.value)
