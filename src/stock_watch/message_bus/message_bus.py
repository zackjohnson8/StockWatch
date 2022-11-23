from .message_queue import MessageQueue
from .message_handler import MessageHandler


class MessageBus(object):
    """Message bus for stock watch.

    The message bus is responsible for sending messages to the
    message queue and receiving messages from the message queue.
    """

    def __init__(self):
        """Initialize the message bus.

        """
        self._message_queue = MessageQueue()
        self._message_handler = MessageHandler()

    def send_message(self, message):
        """Send a message to the message queue.

        Args:
            message: The message to send.
        """
        self._message_queue.send_message(message)

    def receive_message(self):
        """Receive a message from the message queue.

        Returns:
            The message received.
        """
        return self._message_queue.receive_message()

    def handle_message(self, message):
        """Handle a message.

        Args:
            message: The message to handle.
        """
        self._message_handler.handle_message(message)
