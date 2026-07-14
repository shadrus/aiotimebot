from enum import Enum


class GetMaintenanceJobsByTypeType(str, Enum):
    ELASTICSEARCH_POST_INDEXING = "elasticsearch_post_indexing"
    SAASSEARCH_POST_INDEXING = "saassearch_post_indexing"

    def __str__(self) -> str:
        return str(self.value)
