from enum import Enum


class OrganizationUpdateOrganizationPutBodyRegionType(str, Enum):
    INTERNATIONAL = "INTERNATIONAL"
    INTERSTATE = "INTERSTATE"
    LOCAL = "LOCAL"
    NATIONAL = "NATIONAL"
    STATE = "STATE"

    def __str__(self) -> str:
        return str(self.value)
