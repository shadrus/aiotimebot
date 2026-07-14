from enum import IntEnum


class PluginStatusState(IntEnum):
    NOT_RUNNING = 0
    STARTING = 1
    RUNNING = 2
    FAILED_TO_START = 3
    FAILED_TO_STAY_RUNNING = 4
    STOPPING = 5

    def __str__(self) -> str:
        return str(self.value)
