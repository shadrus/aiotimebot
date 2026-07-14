from enum import Enum


class ApplicationCommandRequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
