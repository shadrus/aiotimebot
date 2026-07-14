from enum import Enum


class ApplicationBotAdditionalPermissionsItem(str, Enum):
    POSTALL = "post:all"
    POSTCHANNELS = "post:channels"

    def __str__(self) -> str:
        return str(self.value)
