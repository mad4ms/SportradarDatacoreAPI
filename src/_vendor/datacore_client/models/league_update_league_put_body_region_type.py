from enum import Enum


class LeagueUpdateLeaguePutBodyRegionType(str, Enum):
    INTERNATIONAL = "INTERNATIONAL"
    INTERSTATE = "INTERSTATE"
    LOCAL = "LOCAL"
    NATIONAL = "NATIONAL"
    STATE = "STATE"

    def __str__(self) -> str:
        return str(self.value)
