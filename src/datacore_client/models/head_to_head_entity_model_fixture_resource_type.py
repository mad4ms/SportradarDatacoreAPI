from enum import Enum


class HeadToHeadEntityModelFixtureResourceType(str, Enum):
    FIXTURES = "fixtures"

    def __str__(self) -> str:
        return str(self.value)
