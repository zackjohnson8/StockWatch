import logging
from time import sleep
from .scraper import Scraper
from ..apis import reddit_api
import src.stock_watch.message_bus.message_bus as message_bus
import stock_watch


class RedditScraper(Scraper):

    def __init__(self):
        self._running = False
        self._reddit_api = reddit_api.RedditAPI(site_name="stock_watch_bot")
        self._message_bus = message_bus.MessageBus()
        logging.info(self._reddit_api.user.me())

    def start(self):
        logging.info("Starting RedditScraper")
        self._running = True
        self._start_retrieval_loop()

    def stop(self):
        self._running = False

    def _start_retrieval_loop(self):
        self._running = True
        followed_subreddits = self._get_followed_subreddit_list()
        while self._running:
            sleep(1)
            stock_watch.service_bus.publish(message_bus.MessageTypes.ANALYSIS, f"Followed subreddits: {followed_subreddits}")

    def _get_followed_subreddit_list(self):
        return self._reddit_api.user.subreddits(limit=None)

    @property
    def running(self):
        return self._running
