from enum import Enum


class ImagesModelFileType(str, Enum):
    JPG = "JPG"
    PNG = "PNG"
    SVG = "SVG"

    def __str__(self) -> str:
        return str(self.value)
