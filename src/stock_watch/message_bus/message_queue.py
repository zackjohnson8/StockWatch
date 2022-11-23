from queue import Queue


class MessageQueue(object):
    """Message queue for stock watch.

    The message queue is responsible for sending messages to the
    message bus and receiving messages from the message bus.
    """

    def __init__(self):
        """Initialize the message queue."""
        self._queue = Queue()

    def send_message(self, message):
        """Send a message to the message bus.

        Args:
            message: The message to send.
        """
        self._queue.put(message)

    def receive_message(self):
        """Receive a message from the message bus.

        Returns:
            The message received.
        """
        return self._queue.get()
