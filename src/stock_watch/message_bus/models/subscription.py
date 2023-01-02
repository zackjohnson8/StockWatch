import multiprocessing.connection as connection
from .channel import Channel


class Subscription:

    def __init__(self, channel: Channel, pipe_connection: connection.Connection):
        """
        Create a subscription to a channel.
        :param channel: The channel to subscribe to.
        """
        if not isinstance(channel, Channel) or not isinstance(pipe_connection, connection.Connection):
            raise Exception("The subscription must have a channel and a callback.")

        self.channel = channel
        self.connection = pipe_connection
