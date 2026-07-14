from enum import Enum


class MigrateAuthToSamlBodyFrom(str, Enum):
    EMAIL = "email"
    GITLAB = "gitlab"
    GOOGLE = "google"
    LDAP = "ldap"

    def __str__(self) -> str:
        return str(self.value)
