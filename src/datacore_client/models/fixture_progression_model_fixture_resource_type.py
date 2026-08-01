from enum import Enum


class FixtureProgressionModelFixtureResourceType(str, Enum):
    FIXTURES = "fixtures"

    def __str__(self) -> str:
        return str(self.value)
