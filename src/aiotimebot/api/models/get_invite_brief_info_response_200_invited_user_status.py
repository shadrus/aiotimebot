from enum import Enum


class GetInviteBriefInfoResponse200InvitedUserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
