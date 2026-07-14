from enum import Enum


class PostActionDataSource(str, Enum):
    CHANNELS = "channels"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
