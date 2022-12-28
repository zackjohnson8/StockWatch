from src.stock_watch.message_bus.models import Publish, Subscription
import queue


class MessageQueue:
    def __init__(self):
        """
        A queue to store publish messages that are waiting to be sent to subscribers.
        """
        self._queue = queue.Queue()

    @property
    def queue(self) -> queue.Queue:
        return self._queue

    def add_publish(self, message):
        """
        Add a publish message to the queue.
        :param publish: The publish message to add to the queue.
        :return:
        """
        self._queue.put(message)

    def add_subscription(self, subscription: Subscription):
        """
        Add a subscription to the queue.
        :param subscription: The subscription to add to the queue.
        :return:
        """
        self._queue.put(subscription)

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return self._queue.empty()

    def get(self):
        """
        Pop the first item from the queue.
        :return: The first item from the queue.
        """
        return self._queue.get()