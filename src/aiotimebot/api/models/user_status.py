from enum import Enum


class UserStatus(str, Enum):
    AWAY = "away"
    DND = "dnd"
    OFFLINE = "offline"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
