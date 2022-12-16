import pytest
from src.stock_watch.message_bus import MessageBus
from src.stock_watch.message_bus.models import Publish
from src.stock_watch.message_bus.models.subscription import Subscription
from src.stock_watch.message_bus.models.channel import Channel


def test_WhenMessagebusCreated_OnlyOneInstanceExists():
    # Create two message buses
    message_bus = MessageBus.get_instance()
    message_bus2 = MessageBus.get_instance()

    # Test that the two message buses are the same instance
    assert message_bus.get_instance() == message_bus2.get_instance()


def test_WhenInvalidSubscriptionAdded_ExceptionIsRaised():
    # Create a message bus
    message_bus = MessageBus.get_instance()

    # Create subscription options
    subscription_without_channel = Subscription(channel=None, callback=print)
    subscription_without_callback = Subscription(channel=Channel.RESEARCH, callback=None)
    subscription_without_callback_and_channel = Subscription(channel=None, callback=None)

    # Test that an exception is raised when adding the subscription
    with pytest.raises(Exception):
        message_bus.subscribe(subscription_without_callback)

    with pytest.raises(Exception):
        message_bus.subscribe(subscription_without_channel)

    with pytest.raises(Exception):
        message_bus.subscribe(subscription_without_callback_and_channel)


def test_WhenValidSubscriptionAdded_SubscriptionsUpdated():
    # Create a message bus
    message_bus = MessageBus.get_instance()

    # Create a subscription
    subscription = Subscription(channel=Channel.RESEARCH, callback=print)

    # Add the subscription
    message_bus.subscribe(subscription)

    # Test that the subscription was added
    assert message_bus.has_subscription(subscription)


def test_WhenInvalidPublishSent_ExceptionIsRaised():
    # Create a message bus
    message_bus = MessageBus.get_instance()

    # Create publish options
    publish_without_channel = Publish(channel=None, message="Test")
    publish_without_message = Publish(channel=Channel.RESEARCH, message=None)
    publish_without_channel_and_message = Publish(channel=None, message=None)

    # Test that an exception is raised when adding the publish
    with pytest.raises(Exception):
        message_bus.publish(publish_without_channel)

    with pytest.raises(Exception):
        message_bus.publish(publish_without_message)

    with pytest.raises(Exception):
        message_bus.publish(publish_without_channel_and_message)