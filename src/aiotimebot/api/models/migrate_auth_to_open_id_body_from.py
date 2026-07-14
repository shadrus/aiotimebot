from enum import Enum


class MigrateAuthToOpenIDBodyFrom(str, Enum):
    EMAIL = "email"
    GITLAB = "gitlab"
    GOOGLE = "google"
    LDAP = "ldap"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
