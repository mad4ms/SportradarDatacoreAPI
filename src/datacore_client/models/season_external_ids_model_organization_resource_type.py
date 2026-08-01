from enum import Enum


class SeasonExternalIdsModelOrganizationResourceType(str, Enum):
    ORGANIZATIONS = "organizations"

    def __str__(self) -> str:
        return str(self.value)
