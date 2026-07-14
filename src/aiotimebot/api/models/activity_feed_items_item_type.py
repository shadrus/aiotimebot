from enum import Enum


class ActivityFeedItemsItemType(str, Enum):
    MENTION = "mention"
    REACTION = "reaction"

    def __str__(self) -> str:
        return str(self.value)
