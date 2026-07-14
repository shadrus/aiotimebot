from enum import Enum


class UploadTempFileSource(str, Enum):
    INVITE = "invite"

    def __str__(self) -> str:
        return str(self.value)
