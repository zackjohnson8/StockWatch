from src.stock_watch.message_bus.models import Publish


class MessageQueue:
    def __init__(self):
        """
        A queue to store publish messages that are waiting to be sent to subscribers.
        """
        self._queue = []

    def put(self, publish: Publish) -> None:
        """
        Add a publish message to the queue.
        :param publish: The publish to add to the queue.
        :return:
        """
        self._queue.append(publish)

    def get(self) -> Publish:
        """
        Get the next publish message from the queue.
        :return:
        """
        return self._queue.pop(0)

    def empty(self):
        """
        Check if the queue is empty.
        :return:
        """
        return len(self._queue) == 0
