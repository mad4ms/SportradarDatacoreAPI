from enum import Enum


class FixturePbpEventAddFixturePBPEventPostBodyClass(str, Enum):
    CLOCK = "clock"
    SPORT = "sport"

    def __str__(self) -> str:
        return str(self.value)
