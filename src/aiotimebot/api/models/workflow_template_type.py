from enum import Enum


class WorkflowTemplateType(str, Enum):
    CHANNEL = "channel"
    ME = "me"
    OTHER_CHANNEL = "otherChannel"
    OTHER_USER = "otherUser"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
