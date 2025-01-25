from enum import Enum

class QueryCategory(str, Enum):
    """Enumeration of categories for incoming query.
    Pick specific if the query seeks detailed or pinpointed information
    Pick summary if the query seeks a broad overview or general understanding
    """

    SPECIFIC = "specific"
    SUMMARY = "summary" 