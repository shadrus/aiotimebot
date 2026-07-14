from enum import Enum


class ChannelSuggestionType(str, Enum):
    CHANNEL = "channel"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
