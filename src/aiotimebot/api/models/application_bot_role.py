from enum import Enum


class ApplicationBotRole(str, Enum):
    MEMBER = "member"
    SYSTEM_ADMIN = "system_admin"

    def __str__(self) -> str:
        return str(self.value)
