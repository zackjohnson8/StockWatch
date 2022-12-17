from .channel import Channel
from .message import Message


class Publish(object):
    def __init__(self, channel: Channel, message: Message):
        """
        Create a publish message.
        :param channel: The channel to publish to.
        :param message: The message to publish.
        """
        if not isinstance(channel, Channel) or not isinstance(message, Message):
            raise Exception("The publish must have a channel and a message.")

        self.channel = channel
        self.message = message
