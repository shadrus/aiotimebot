from enum import Enum


class WorkflowStepType(str, Enum):
    SEND_MESSAGE_TO_CHANNEL = "sendMessageToChannel"
    SEND_TEMPLATE_MESSAGE = "sendTemplateMessage"

    def __str__(self) -> str:
        return str(self.value)
