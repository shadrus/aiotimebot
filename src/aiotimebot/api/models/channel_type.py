from enum import Enum


class ChannelType(str, Enum):
    DIRECT = "D"
    GROUP = "G"
    OPEN = "O"
    PRIVATE = "P"

    def __str__(self) -> str:
        return str(self.value)
