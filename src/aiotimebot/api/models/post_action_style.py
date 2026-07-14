from enum import Enum


class PostActionStyle(str, Enum):
    DANGER = "danger"
    DEFAULT = "default"
    GOOD = "good"
    PRIMARY = "primary"
    SUCCESS = "success"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
