from enum import Enum


class GetInviteBriefInfoResponse200InviteType(str, Enum):
    GUEST_INVITE = "guest-invite"
    MEMBER_INVITE = "member-invite"

    def __str__(self) -> str:
        return str(self.value)
