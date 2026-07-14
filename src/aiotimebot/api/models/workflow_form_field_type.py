from enum import Enum


class WorkflowFormFieldType(str, Enum):
    BOOL = "bool"
    RADIO = "radio"
    SELECT = "select"
    TEXT = "text"
    TEXT_AREA = "textarea"

    def __str__(self) -> str:
        return str(self.value)
