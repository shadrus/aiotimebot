from enum import Enum


class ChannelTypeForTeam(str, Enum):
    GROUP = "G"
    OPEN = "O"
    PRIVATE = "P"

    def __str__(self) -> str:
        return str(self.value)
