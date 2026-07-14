from enum import Enum


class SearchIndexType(str, Enum):
    CHANNEL = "channel"
    FILE = "file"
    HASHTAG = "hashtag"
    POST = "post"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
