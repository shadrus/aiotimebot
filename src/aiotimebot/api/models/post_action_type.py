from enum import Enum


class PostActionType(str, Enum):
    BUTTON = "button"
    SELECT = "select"

    def __str__(self) -> str:
        return str(self.value)
