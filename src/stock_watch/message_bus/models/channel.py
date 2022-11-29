from enum import Enum


class Channel(Enum):
    """
    The channel that a message is published on. The channel is used to route messages.
    """
    RESEARCH = 1
    ANALYSIS = 2
    TRADING = 3
    DATABASE = 4
