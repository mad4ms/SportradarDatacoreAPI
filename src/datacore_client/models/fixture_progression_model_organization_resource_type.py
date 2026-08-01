from enum import Enum


class FixtureProgressionModelOrganizationResourceType(str, Enum):
    ORGANIZATIONS = "organizations"

    def __str__(self) -> str:
        return str(self.value)
