from enum import Enum


class SidebarCategorySorting(str, Enum):
    ALPHABETICAL = "alpha"
    DEFAULT = ""
    MANUAL = "manual"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
