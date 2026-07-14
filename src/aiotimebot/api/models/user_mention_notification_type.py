from enum import Enum


class UserMentionNotificationType(str, Enum):
    ALL = "all"
    MENTION = "mention"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
