from enum import Enum


class StandingProgressionsModelPoolResourceType(str, Enum):
    SEASONPOOLS = "seasonPools"

    def __str__(self) -> str:
        return str(self.value)
