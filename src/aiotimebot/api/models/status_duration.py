from enum import Enum


class StatusDuration(str, Enum):
    DATE_AND_TIME = "date_and_time"
    FOUR_HOURS = "four_hours"
    ONE_HOUR = "one_hour"
    THIRTY_MINUTES = "thirty_minutes"
    THIS_WEEK = "this_week"
    TODAY = "today"

    def __str__(self) -> str:
        return str(self.value)
