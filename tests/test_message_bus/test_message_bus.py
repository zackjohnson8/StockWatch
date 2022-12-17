import json
import pytest

from src.stock_watch.message_bus import MessageBus
from src.stock_watch.message_bus.models import Publish
from src.stock_watch.message_bus.models.subscription import Subscription
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.message import Message


def test_WhenMessagebusCreated_OnlyOneInstanceExists():
    # Create two message buses
    message_bus = MessageBus.get_instance()
    message_bus2 = MessageBus.get_instance()

    # Test that the two message buses are the same instance
    assert message_bus.get_instance() == message_bus2.get_instance()


def test_WhenInvalidSubscriptionAdded_ExceptionIsRaised():
    # Create a message bus
    message_bus = MessageBus.get_instance()

    # Test that an exception is raised when adding the subscription
    with pytest.raises(Exception):
        message_bus.subscribe(subscription="not a subscription")


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

    # Test that an exception is raised when adding the publish method
    with pytest.raises(Exception):
        message_bus.publish(publish='not a publish')


def test_CreateMessageWithValidInformation_IsSuccessful():
    json_string = '{ "name":"John", "age":30, "city":"New York"}'
    json_dict = json.loads(json_string)

    # assert that the message is created successfully
    message = Message(header='reddit_submission', data_model=json_dict)
    assert message.header == 'reddit_submission'
    assert message.data_model == json_dict


#noinspection PyTypeChecker
def test_CreateMessageWithInvalidInformation_ExceptionIsRaised():
    # Test that an exception is raised when creating the message with invalid information
    with pytest.raises(Exception):
        Message(header='reddit_submission', data_model='not a dict')

    with pytest.raises(Exception):
        Message(header=123, data_model='not a dict')

    with pytest.raises(Exception):
        Message(header=123, data_model={'test': 'test'})

def test_CreatePublishWithValidInformation_IsSuccessful():
    # Create a message
    json_string = '{ "name":"John", "age":30, "city":"New York"}'
    json_dict = json.loads(json_string)
    message = Message(header='reddit_submission', data_model=json_dict)

    # assert that the publish is created successfully
    publish = Publish(channel=Channel.RESEARCH, message=message)
    assert publish.channel == Channel.RESEARCH
    assert publish.message == message


#noinspection PyTypeChecker
def test_CreatePublishWithInvalidInformation_ExceptionIsRaised():
    # Test that an exception is raised when creating the publish with invalid information
    with pytest.raises(Exception):
        Publish(channel='not a channel', message='not a message')

    with pytest.raises(Exception):
        Publish(channel=Channel.RESEARCH, message='not a message')

    with pytest.raises(Exception):
        Publish(channel='not a channel', message=Message(header='reddit_submission', data_model={'test': 'test'}))


# TODO: When multiprocess attempts to call the callback, it fails. This is because the callback is a function that is
#  defined in the test file. The callback is not defined in the multiprocess file. This is a known issue with
#  multiprocess.
# def test_WhenMultipleSubscribersExist_AllSubscribersReceiveMessage():
#     # Create a message bus
#     message_bus = MessageBus.get_instance()
#
#     # Create callbacks
#     callback1 = mock.Mock()
#     callback2 = mock.Mock()
#
#     # Create subscriptions
#     subscription1 = Subscription(channel=Channel.RESEARCH, callback=callback1)
#     subscription2 = Subscription(channel=Channel.RESEARCH, callback=callback2)
#
#     # Add the subscriptions
#     message_bus.subscribe(subscription1)
#     # message_bus.subscribe(subscription2)
#
#     # Create a publish
#     publish = Publish(channel=Channel.RESEARCH, message=Message(header="Test", data_model={'test': 'test'}))
#
#     # Publish the message
#     message_bus.publish(publish)
#     time.sleep(3)
#
#     # Assert that the message was published to all subscribers
#     callback1.assert_called_once()
#     callback2.assert_called_with()
