from enum import Enum


class MigrateAuthToLdapBodyMatchField(str, Enum):
    EMAIL = "email"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
