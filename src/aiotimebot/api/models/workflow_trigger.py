from enum import Enum


class WorkflowTrigger(str, Enum):
    MANUAL = "manual"
    REACTION = "reaction"
    TIME = "time"
    USER_JOINED_CHANNEL = "userJoinedChannel"

    def __str__(self) -> str:
        return str(self.value)
