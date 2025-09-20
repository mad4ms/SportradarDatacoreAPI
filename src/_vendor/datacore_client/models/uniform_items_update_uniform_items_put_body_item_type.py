from enum import Enum


class UniformItemsUpdateUniformItemsPutBodyItemType(str, Enum):
    BOTTOM = "BOTTOM"
    GOALKEEPER_BOTTOM = "GOALKEEPER_BOTTOM"
    GOALKEEPER_TOP = "GOALKEEPER_TOP"
    HELMET = "HELMET"
    SOCKS = "SOCKS"
    TOP = "TOP"
    WARMUP_BOTTOM = "WARMUP_BOTTOM"
    WARMUP_TOP = "WARMUP_TOP"

    def __str__(self) -> str:
        return str(self.value)
