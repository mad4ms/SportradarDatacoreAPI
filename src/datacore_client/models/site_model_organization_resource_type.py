from enum import Enum


class SiteModelOrganizationResourceType(str, Enum):
    ORGANIZATIONS = "organizations"

    def __str__(self) -> str:
        return str(self.value)
