from enum import Enum


class SiteExternalIdsModelSiteResourceType(str, Enum):
    SITES = "sites"

    def __str__(self) -> str:
        return str(self.value)
