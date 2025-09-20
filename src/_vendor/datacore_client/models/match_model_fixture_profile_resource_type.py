from enum import Enum


class MatchModelFixtureProfileResourceType(str, Enum):
    FIXTUREPROFILES = "fixtureProfiles"

    def __str__(self) -> str:
        return str(self.value)
