from enum import Enum


class LeagueListRegionType(str, Enum):
    INTERNATIONAL = "INTERNATIONAL"
    LOCAL = "LOCAL"
    NATIONAL = "NATIONAL"
    STATE = "STATE"

    def __str__(self) -> str:
        return str(self.value)
