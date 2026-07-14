from enum import Enum


class SortOption(str, Enum):
    CREATEASC = "CreateAsc"
    CREATEDESC = "CreateDesc"
    SCOREDESC = "ScoreDesc"

    def __str__(self) -> str:
        return str(self.value)
