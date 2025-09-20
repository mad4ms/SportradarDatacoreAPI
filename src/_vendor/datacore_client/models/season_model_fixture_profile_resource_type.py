from enum import Enum


class SeasonModelFixtureProfileResourceType(str, Enum):
    FIXTUREPROFILES = "fixtureProfiles"

    def __str__(self) -> str:
        return str(self.value)
