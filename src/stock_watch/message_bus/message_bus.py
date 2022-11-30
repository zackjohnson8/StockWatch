import multiprocessing
import dill as pickle

from .message_bus_process import MessageBusProcess
from .models.subscription import Subscription
from .models.publish import Publish
from .message_bus_service import MessageBusService


class MessageBus(object):
    __instance = None

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of the message bus.
        :return:
        """
        if MessageBus.__instance is None:
            MessageBus()
        return MessageBus.__instance

    def __init__(self):
        """
        A message bus to handle subscriptions and publishes.
        """
        if MessageBus.__instance is None:
            MessageBus.__instance = self
            self._service = MessageBusService()
            self._parent_conn, self._child_conn = multiprocessing.Pipe(duplex=True)
            self._queue_process = MessageBusProcess(target=self._service.start_listening_to_pipe,
                                                    args=(self._child_conn,))

    def start(self):
        """
        Start the message bus process.
        :return:
        """
        if not self._queue_process.is_alive():
            self._queue_process.start()

    def subscribe(self, subscriptions: [Subscription]):
        """
        Subscribe to a channel.
        :param subscriptions: The list of subscription objects to add.
        :return:
        """
        for subscription in subscriptions:
            pickled = pickle.dumps(subscription)
            self._parent_conn.send(pickled)

    def publish(self, publish: Publish):
        """
        Publish a message to subscribers.
        :param publish: The publish message to send to subscribers.
        :return:
        """
        pickled = pickle.dumps(publish)
        self._parent_conn.send(pickled)
