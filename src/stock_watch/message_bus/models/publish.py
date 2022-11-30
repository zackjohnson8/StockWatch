from .channel import Channel
from .message import Message


class Publish(object):
    def __init__(self, channel: Channel, message: Message):
        """
        Create a publish message.
        :param channel: The channel to publish to.
        :param message: The message to publish.
        """
        self.channel = channel
        self.message = message
