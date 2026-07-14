from enum import Enum


class MigrateAuthToLdapBodyFrom(str, Enum):
    EMAIL = "email"
    GITLAB = "gitlab"
    GOOGLE = "google"
    OPENID = "openid"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
