from enum import Enum


class EntityInsertTeamPostBodyStandardType3Type1(str, Enum):
    ELITE = "ELITE"
    FRIENDLY = "FRIENDLY"
    GRASS_ROOT = "GRASS_ROOT"
    INTERNATIONAL = "INTERNATIONAL"
    NONCONTINENTAL_CHAMPIONSHIP = "NONCONTINENTAL_CHAMPIONSHIP"
    OLYMPIC = "OLYMPIC"
    REGION = "REGION"
    TIER2 = "TIER2"
    TIER3 = "TIER3"
    WORLD_CHAMPIONSHIP = "WORLD_CHAMPIONSHIP"
    ZONE_CHAMPIONSHIP = "ZONE_CHAMPIONSHIP"

    def __str__(self) -> str:
        return str(self.value)
