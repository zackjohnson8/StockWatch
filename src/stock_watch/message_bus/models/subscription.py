from multiprocessing.connection import Connection
from .channel import Channel


class Subscription:

    def __init__(self, channel: Channel, connection: Connection):
        """
        Create a subscription to a channel.
        :param channel: The channel to subscribe to.
        """
        if not isinstance(channel, Channel) or not isinstance(connection, Connection):
            raise Exception("The subscription must have a channel and a callback.")

        self.channel = channel
        self.connection = connection
