from enum import Enum


class ConductModelConductTypeItem(str, Enum):
    CITATION = "CITATION"
    CONCUSSION = "CONCUSSION"
    CORRUPTION = "CORRUPTION"
    DOPING = "DOPING"
    MATCH_FIXING = "MATCH_FIXING"
    SWEARING = "SWEARING"
    UNSPORTSMANLIKE_CONDUCT = "UNSPORTSMANLIKE_CONDUCT"
    VIOLENT_CONDUCT = "VIOLENT_CONDUCT"

    def __str__(self) -> str:
        return str(self.value)
