from enum import Enum


class FixturePBPEventModelFixtureResourceType(str, Enum):
    FIXTURES = "fixtures"

    def __str__(self) -> str:
        return str(self.value)
