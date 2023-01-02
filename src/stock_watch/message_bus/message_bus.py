from src.stock_watch.message_bus.message_queue import MessageQueue
from .message_consumer import MessageConsumer
from .models.subscription import Subscription
from .models.publish import Publish


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
            self.message_consumer = MessageConsumer()
        else:
            raise Exception("Only one instance of the message bus can exist. Call MessageBus.get_instance() to get the "
                            "singleton instance.")

    def subscribe(self, subscription: Subscription):
        if not isinstance(subscription, Subscription):
            raise Exception("The subscription must be of type Subscription.")

        self.message_consumer.add_subscription(subscription=subscription)

    def publish(self, publish: Publish):
        """
        Publish a message to subscribers.
        :param publish: The published message to send to subscribers.
        :return:
        """
        if not isinstance(publish, Publish):
            raise Exception("The publish must be of type Publish.")

        self.message_consumer.add_to_queue(message=publish)

    def start(self):
        """
        Start the message bus.
        :return:
        """
        self.message_consumer.start()

    def add_connection(self, connection):
        self.message_consumer.add_connection(connection=connection)

    def has_subscription(self, subscription: Subscription):
        return self.message_consumer.has_subscription(subscription=subscription)