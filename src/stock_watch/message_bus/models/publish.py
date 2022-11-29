from .channel import Channel
from .message import Message


class Publish(object):
    def __init__(self, channel: Channel, message: Message):
        self.channel = channel
        self.message = message
