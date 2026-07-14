from enum import Enum


class AutocompleteUsersSource(str, Enum):
    SEARCH_USER = "search-user"
    TAG_USER = "tag-user"

    def __str__(self) -> str:
        return str(self.value)
