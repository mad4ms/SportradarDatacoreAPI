from enum import Enum


class SeriesModelPoolResourceType(str, Enum):
    SEASONPOOLS = "seasonPools"

    def __str__(self) -> str:
        return str(self.value)
