from enum import Enum


class MessageTypes(Enum):
    """Message types for stock watch"""
    RESEARCH = 0
    ANALYSIS = 1
    TRADING = 2
    DATABASE = 3
