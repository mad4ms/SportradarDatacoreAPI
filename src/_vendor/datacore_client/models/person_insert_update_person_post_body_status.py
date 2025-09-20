from enum import Enum


class PersonInsertUpdatePersonPostBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DECEASED = "DECEASED"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"
    UNREGISTERED = "UNREGISTERED"

    def __str__(self) -> str:
        return str(self.value)
