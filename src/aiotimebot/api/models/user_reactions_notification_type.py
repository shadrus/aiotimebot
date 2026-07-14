from enum import Enum


class UserReactionsNotificationType(str, Enum):
    CONVERSATION = "conversation"
    DIRECT = "direct"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
