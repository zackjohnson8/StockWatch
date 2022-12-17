from typing import Callable

from .channel import Channel


class Subscription:

    def __init__(self, channel: Channel, callback: Callable):
        """
        Create a subscription to a channel.
        :param channel: The channel to subscribe to.
        :param callback: The callback to call when a message is published to the channel.
        """
        if not isinstance(channel, Channel) or not callable(callback):
            raise Exception("The subscription must have a channel and a callback.")

        self.channel = channel
        self.callback = callback
