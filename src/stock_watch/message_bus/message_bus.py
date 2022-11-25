from typing import Any
from .models.types import MessageTypes

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
        return list(subscription.keys())[0].value == message_type.value


    def _call_subscription_callback(self, subscription: {}, message: Any):
        callback = list(subscription.values())[0]
        callback(message)
