from enum import Enum


class VideoFileModelResolution(str, Enum):
    VALUE_0 = "288"
    VALUE_1 = "720"
    VALUE_2 = "1080"

    def __str__(self) -> str:
        return str(self.value)
