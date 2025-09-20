from enum import Enum


class MatchModelRoundResourceType(str, Enum):
    SEASONROUNDS = "seasonRounds"

    def __str__(self) -> str:
        return str(self.value)
