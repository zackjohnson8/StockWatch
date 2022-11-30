import logging
import dill as pickle
from src.stock_watch.message_bus.models.subscription import Subscription
from src.stock_watch.message_bus.models.publish import Publish
from .message_queue import MessageQueue


class MessageBusService(object):
    def __init__(self):
        """
        Use this class as a process service with a pipe connection to the parent process. Subscriptions and publishes
        will be sent to this process through the pipe connection. This process will then handle the subscriptions and
        publishes.
        """
        self._queue = MessageQueue()
        self._subscriptions = []

    def _subscribe(self, subscription: Subscription):
        """
        Subscribe to a channel.
        :param subscription: The subscription to add.
        :return:
        """
        self._subscriptions.append(subscription)

    def _publish(self, publish: Publish):
        """
        Publish a message to subscribers.
        :param publish: The publish message to send to subscribers.
        :return:
        """
        for subscription in self._subscriptions:
            if subscription.channel == publish.channel:
                callback = subscription.callback
                callback(message=publish.message)

    def start_listening_to_pipe(self, conn):
        """
        Start listening to the pipe connection for subscriptions and publishes.
        :param conn: The pipe connection to listen to.
        :return:
        """
        # TODO: Implement concurrency
        while True:
            if conn.poll():
                message = conn.recv()
                if isinstance(message, bytes):
                    message = pickle.loads(message)

                # isinstance not working with deserialized objects. This is a workaround.
                message_class_name = message.__class__.__name__

                if message_class_name == 'Subscription':
                    self._subscribe(subscription=message)
                elif message_class_name == 'Publish':
                    self._queue.put(message)
                else:
                    logging.error(f"MessageBus received an unknown message type: {type(message)}")
            else:
                if not self._queue.empty():
                    publish = self._queue.get()
                    self._publish(publish=publish)

    def _send_message_to_subscribers(self, publish: Publish):
        """
        Send a publish message to all subscribers that are subscribed to the publish channel.
        :param publish: The publish message to send to subscribers.
        :return:
        """
        for subscription in self._subscriptions:
            if subscription.channel == publish.channel:
                subscription.callback(publish.message)
