import json


class Message(object):
    """
    A message is a class that encapsulates data that is sent over the message bus channel.
    """

    def __init__(self, header: str, data_model: json):
        """
        :param header: The header of the message. This is used to identify the type of message.
        :param data_model: The data model of the message.
        """
        self.header = header
        self.data_model = data_model
