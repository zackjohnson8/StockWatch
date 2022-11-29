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
        if MessageBus.__instance is None:
            MessageBus()
        return MessageBus.__instance

    def __init__(self):
        if MessageBus.__instance is None:
            MessageBus.__instance = self
            self._service = MessageBusService()
            self._parent_conn, self._child_conn = multiprocessing.Pipe(duplex=True)
            self._queue_process = MessageBusProcess(target=self._service.start_listening_to_pipe,
                                                    args=(self._child_conn,))

    def start(self):
        if not self._queue_process.is_alive():
            self._queue_process.start()

    def subscribe(self, subscriptions: [Subscription]):
        for subscription in subscriptions:
            pickled = pickle.dumps(subscription)
            self._parent_conn.send(pickled)

    def publish(self, publish: Publish):
        pickled = pickle.dumps(publish)
        self._parent_conn.send(pickled)
