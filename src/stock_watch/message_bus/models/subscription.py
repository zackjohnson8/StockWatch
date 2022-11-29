from typing import Callable

from .channel import Channel


class Subscription:

    def __init__(self, channel: Channel, callback: Callable):
        self.channel = channel
        self.callback = callback

    def __str__(self):
        return f"Subscription(channel={self.channel}, callback={self.callback})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.channel == other.channel and self.callback == other.callback

    def __hash__(self):
        return hash((self.channel, self.callback))
