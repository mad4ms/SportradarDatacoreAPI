from enum import Enum


class RoleModelFixtureResourceType(str, Enum):
    FIXTURES = "fixtures"

    def __str__(self) -> str:
        return str(self.value)
