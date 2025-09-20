from enum import Enum


class SeasonVenuesModelSiteResourceType(str, Enum):
    SITES = "sites"

    def __str__(self) -> str:
        return str(self.value)
