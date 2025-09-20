from enum import Enum


class MatchTeamPeriodStatisticsModelFixtureResourceType(str, Enum):
    FIXTURES = "fixtures"

    def __str__(self) -> str:
        return str(self.value)
