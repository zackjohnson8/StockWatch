from typing import Any


class Message(object):
    """
    A message is a class that encapsulates data that is sent over the message bus channel.
    """

    def __init__(self, header: str, data_model: Any):
        """
        :param header: The header of the message. This is used to identify the type of message.
        :param data: The data should be
        """
        self.header = header
        self.data_model = data_model
