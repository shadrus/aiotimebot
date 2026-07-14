from enum import Enum


class MultiSearchUsersChannelsChannelTypesItem(str, Enum):
    G = "G"
    O = "O"
    P = "P"

    def __str__(self) -> str:
        return str(self.value)
