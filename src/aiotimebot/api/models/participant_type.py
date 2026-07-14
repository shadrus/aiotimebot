from enum import Enum


class ParticipantType(str, Enum):
    BOT = "bot"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
