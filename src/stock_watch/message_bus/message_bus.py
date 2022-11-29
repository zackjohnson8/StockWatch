import multiprocessing
import dill as pickle

from .message_bus_process import MessageBusProcess
from .models.subscription import Subscription
from .models.publish import Publish
from .message_bus_service import MessageBusService


class MessageBus(object):

    def __init__(self):
        # Creating the pipe with duplex because I want verification that the message was received
        self._service = MessageBusService()
        self._parent_conn, self._child_conn = multiprocessing.Pipe(duplex=True)
        self._queue_process = MessageBusProcess(target=self._service.start_listening_to_pipe, args=(self._child_conn,))

    def start(self):
        if not self._queue_process.is_alive():
            self._queue_process.start()

    def subscribe(self, subscriptions: [Subscription]):
        # TODO: Add subscription to a channel
        for subscription in subscriptions:
            pickled = pickle.dumps(subscription)
            self._parent_conn.send(pickled)

    def publish(self, publish: Publish):
        # TODO: Publish to the channel that is specified in publish
        pickled = pickle.dumps(publish)
        self._parent_conn.send(pickled)
