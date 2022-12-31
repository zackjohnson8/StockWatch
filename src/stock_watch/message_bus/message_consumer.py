from src.stock_watch.message_bus.message_queue import MessageQueue
from src.stock_watch.message_bus.models import Publish


class MessageConsumer(object):
    def __init__(self):
        """
        A consumer to consume messages from the message queue.
        """
        self._connections = []
        self._subscriptions = []
        self._message_queue = MessageQueue()

    def start(self):
        """
        Start the consumer.
        :return:
        """
        while True:
            for publish in self._connections:
                if publish.poll():
                    message = publish.recv()
                    self.add_to_queue(message=message)

            if not self._message_queue.is_empty():
                message = self._message_queue.get()
                if isinstance(message, Publish):
                    self.publish_to_subscribers(publish=message)
                else:
                    raise Exception("Unknown message type: {}".format(message))

    def add_subscription(self, subscription):
        self._subscriptions.append(subscription)

    def add_connection(self, connection):
        self._connections.append(connection)

    def publish_to_subscribers(self, publish: Publish):
        if len(self._subscriptions) > 0:
            for subscription in self._subscriptions:
                if subscription.channel == publish.channel:
                    subscription.connection.send(publish)

    def add_to_queue(self, message):
        self._message_queue.add_publish(message=message)
