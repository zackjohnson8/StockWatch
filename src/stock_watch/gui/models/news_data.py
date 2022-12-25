import logging
from src.stock_watch.message_bus.message_bus import MessageBus
from src.stock_watch.message_bus.models import Subscription, Channel


class NewsData:
    def __init__(self):
        self.posted_news = []

        self.message_bus = MessageBus.get_instance()
        news_subscription = Subscription(Channel.RESEARCH, self.on_news)
        self.message_bus.subscribe(news_subscription)

    def on_news(self, message):
        self.posted_news.append(message)
        logging.info('Received research message: {author} posted {title} from {url}'.format(
                author=message.data_model['name'],
                title=message.data_model['title'],
                url=message.data_model['url']))