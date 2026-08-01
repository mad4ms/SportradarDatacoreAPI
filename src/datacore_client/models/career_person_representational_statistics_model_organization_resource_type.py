from enum import Enum


class CareerPersonRepresentationalStatisticsModelOrganizationResourceType(str, Enum):
    ORGANIZATIONS = "organizations"

    def __str__(self) -> str:
        return str(self.value)
