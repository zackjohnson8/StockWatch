from typing import Any
from enum import Enum


# MessageTypes
class MessageTypes(Enum):
    """Message types for stock watch."""
    RESEARCH = 0
    ANALYSIS = 1
    TRADING = 2
    DATABASE = 3


class MessageBus(object):
    _subscriptions = None

    def __init__(self):
        self._subscriptions = []

    def subscribe(self, message_type: MessageTypes, callback: ()):
        self._subscriptions.append({message_type: callback})

    def publish(self, message_type: MessageTypes, message: Any):
        self._send_message_to_subscribers(message_type, message)

    def _send_message_to_subscribers(self, message_type: MessageTypes, message: Any):
        for subscription in self._subscriptions:
            if self._is_subscribed_to_message_type(subscription=subscription, message_type=message_type):
                self._call_subscription_callback(subscription=subscription, message=message)

    def _is_subscribed_to_message_type(self, subscription: {}, message_type: MessageTypes):
        for subscription in self._subscriptions:
            subscription_type = self._get_subscription_type(subscription)
            if subscription_type.value == message_type.value:
                return True
        return False

    def _get_subscription_type(self, subscription: {}):
        return list(subscription.keys())[0]

    def _call_subscription_callback(self, subscription: {}, message: Any):
        callback = list(subscription.values())[0]
        callback(message)
