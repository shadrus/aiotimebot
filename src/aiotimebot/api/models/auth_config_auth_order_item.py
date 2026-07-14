from enum import Enum


class AuthConfigAuthOrderItem(str, Enum):
    EMAIL = "email"
    LDAP = "ldap"
    OPENID = "openid"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)
