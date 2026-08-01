from enum import Enum


class IncludedDataResourcesAdditionalProperty(str, Enum):
    LEAGUE = "league"
    ORGANISATION = "organisation"
    PERSONS = "persons"

    def __str__(self) -> str:
        return str(self.value)
