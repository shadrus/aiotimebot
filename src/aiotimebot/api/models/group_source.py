from enum import Enum


class GroupSource(str, Enum):
    CUSTOM = "custom"
    LDAP = "ldap"

    def __str__(self) -> str:
        return str(self.value)
