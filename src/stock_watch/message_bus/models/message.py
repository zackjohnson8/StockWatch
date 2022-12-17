class Message(object):
    """
    A message is a class that encapsulates data that is sent over the message bus channel.
    """

    def __init__(self, header: str, data_model: dict):
        """
        :param header: The header of the message. This is used to identify the type of message.
        :param data_model: A dictionary that contains the data of the message.
        """
        if not isinstance(header, str) or not isinstance(data_model, dict):
            raise Exception("The message must have a header and a data model.")

        self.header = header
        self.data_model = data_model
