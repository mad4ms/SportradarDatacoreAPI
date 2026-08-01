from enum import Enum


class MatchRosterModelOrganizationResourceType(str, Enum):
    ORGANIZATIONS = "organizations"

    def __str__(self) -> str:
        return str(self.value)
