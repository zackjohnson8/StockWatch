import multiprocessing
import dill as pickle

from stock_watch.message_bus.message_bus_process import MessageBusProcess
from .message_queue import MessageQueue
from stock_watch.message_bus.models.subscription import Subscription
from stock_watch.message_bus.models.publish import Publish
import logging


class MessageBus(object):

    def __init__(self):
        self._parent_conn, self._child_conn = multiprocessing.Pipe(duplex=True)
        self._queue_process = MessageBusProcess(target=self._start_queue_process, args=(self._child_conn,))
        self._queue = MessageQueue()
        self._subscriptions = []

    #
    def start(self):
        if not self._queue_process.is_alive():
            self._queue_process.start()

    def _process_subscribe(self, subscription: Subscription):
        self._subscriptions.append(subscription)

    def _process_publish(self, publish: Publish):
        for subscription in self._subscriptions:
            if subscription.channel == publish.channel:
                callback = subscription.callback
                callback(message=publish.message)

    def _start_queue_process(self, conn):
        # TODO: Implement concurrency
        while True:
            message = conn.recv()

            # if message is bytes then deserialize
            if isinstance(message, bytes):
                message = pickle.loads(message)

            if isinstance(message, Subscription):
                logging.info(f"Subscribed to {message.channel}")
                self._process_subscribe(subscription=message)
            elif isinstance(message, Publish):
                logging.info(f"Published to {message.channel}")
                self._process_publish(publish=message)
            else:
                logging.error(f"MessageBus received an unknown message type: {type(message)}")

    def subscribe(self, subscriptions: [Subscription]):
        for subscription in subscriptions:
            pickled = pickle.dumps(subscription)
            self._parent_conn.send(pickled)

    def publish(self, publish: Publish):
        pickled = pickle.dumps(publish)
        self._parent_conn.send(pickled)

    def _send_message_to_subscribers(self, publish: Publish):
        for subscription in self._subscriptions:
            if subscription.channel == publish.channel:
                subscription.callback(publish.message)
