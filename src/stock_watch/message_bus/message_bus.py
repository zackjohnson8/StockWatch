import multiprocessing
import dill as pickle

from .message_bus_process import MessageBusProcess
from .models.subscription import Subscription
from .models.publish import Publish
from .message_bus_handler import MessageBusHandler


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
            self._subscriptions = []

            # Create a handler to handle subscriptions and publishes
            self.message_handler = MessageBusHandler()

            # Create a multiprocessing pipe to handle communication between the
            # parent(self) and child(MessageBusProcess)
            self._parent_conn, self._child_conn = multiprocessing.Pipe(duplex=True)

            # Create a message_process to be started when ready
            self.message_process = None
        else:
            raise Exception("Only one instance of the message bus can exist. Call MessageBus.get_instance() to get the "
                            "singleton instance.")

    def start(self):
        if not self.message_process:
            self.message_process = MessageBusProcess(target=self.message_handler.start_listening_to_pipe,
                                                     args=(self._child_conn,))
            self.message_process.start()

    def subscribe(self, subscription: Subscription):
        """
        Subscribe to a channel.
        :param subscription: A subscription to be notified if anything is published to the subscription channel.
        :return:
        """
        if not isinstance(subscription, Subscription):
            raise Exception("The subscription must be a Subscription object.")

        # Save the subscription to the list of subscriptions to reference later
        self._subscriptions.append(subscription)

        pickled = pickle.dumps(subscription)
        # Send the pickled subscription object to the child process (message_handler)
        self._parent_conn.send(pickled)

    def publish(self, publish: Publish):
        """
        Publish a message to subscribers.
        :param publish: The published message to send to subscribers.
        :return:
        """
        if not isinstance(publish, Publish):
            raise Exception("The publish must be a Publish object.")

        pickled = pickle.dumps(publish)
        # Send the pickled publish object to the child process (message_handler)
        self._parent_conn.send(pickled)

    def has_subscription(self, subscription: Subscription):
        """
        Check if a subscription exists.
        :param subscription: The subscription to check for.
        :return:
        """
        return subscription in self._subscriptions
