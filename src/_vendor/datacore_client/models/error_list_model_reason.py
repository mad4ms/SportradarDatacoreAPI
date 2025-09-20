from enum import Enum


class ErrorListModelReason(str, Enum):
    DELETE_ERROR = "DELETE_ERROR"
    ERROR = "ERROR"
    INVALID_DATA = "INVALID_DATA"
    NOT_AUTHORISED = "NOT_AUTHORISED"
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
