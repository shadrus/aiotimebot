from enum import Enum


class WorkflowFormFieldDataSource(str, Enum):
    CHANNELS = "channels"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
