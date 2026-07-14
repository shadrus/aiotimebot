from enum import Enum


class NewChannelType(str, Enum):
    OPEN = "O"
    PRIVATE = "P"

    def __str__(self) -> str:
        return str(self.value)
