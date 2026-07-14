from enum import Enum


class RegenApplicationTokenTokenType(str, Enum):
    BOT = "bot"
    COMMAND = "command"

    def __str__(self) -> str:
        return str(self.value)
