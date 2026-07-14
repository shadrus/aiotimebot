from enum import Enum


class GetActivityFeedSortBy(str, Enum):
    ACTIVITY_AT = "activity_at"
    POSTED_AT = "posted_at"

    def __str__(self) -> str:
        return str(self.value)
