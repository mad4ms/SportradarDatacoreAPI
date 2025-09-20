from enum import Enum


class FixturePBPEventModelEntityResourceType(str, Enum):
    ENTITIES = "entities"

    def __str__(self) -> str:
        return str(self.value)
