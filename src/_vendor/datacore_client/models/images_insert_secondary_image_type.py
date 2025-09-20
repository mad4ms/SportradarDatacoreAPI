from enum import Enum


class ImagesInsertSecondaryImageType(str, Enum):
    LOGO = "LOGO"
    LOGO_ALTERNATE = "LOGO_ALTERNATE"
    LOGO_BACKGROUND = "LOGO_BACKGROUND"
    PERSON_HEAD = "PERSON_HEAD"
    PERSON_POSE = "PERSON_POSE"
    PERSON_WAIST = "PERSON_WAIST"
    TEAM_PHOTO = "TEAM_PHOTO"
    UNIFORM = "UNIFORM"
    UNIFORM_ITEM = "UNIFORM_ITEM"

    def __str__(self) -> str:
        return str(self.value)
