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
        for subscription in self._subscriptions:
            subscription_type = list(subscription.keys())[0]
            if subscription_type.value == message_type.value:
                call_back = subscription[subscription_type]
                call_back(message)
