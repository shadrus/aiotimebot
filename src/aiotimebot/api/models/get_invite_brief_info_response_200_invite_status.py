from enum import Enum


class GetInviteBriefInfoResponse200InviteStatus(str, Enum):
    EXPIRED = "expired"
    REVOKED = "revoked"
    USED = "used"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
