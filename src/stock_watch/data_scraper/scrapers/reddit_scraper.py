import logging
from time import sleep
from .scraper import Scraper
from ..apis import reddit_api
import src.stock_watch.message_bus.message_bus as message_bus
import src.stock_watch as stock_watch
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.message import Message
from ..configs.config import Config


class RedditScraper(Scraper):

    def __init__(self):
        """
        The RedditScraper is a scraper that scrapes data from Reddit. This uses the Reddit API provided from PRAW.
        """
        self._config = Config()
        self._running = False
        self._reddit_api = None
        self._message_bus = stock_watch.message_bus.get_instance()
        self.site_name = "stock_watch_bot"

    def start(self):
        """
        Starts the RedditScraper. Cannot start without updating the praw.ini file with the correct credentials.
        :return:
        """
        logging.info("Starting RedditScraper")
        # Validate that the praw.ini has site_name and the required fields
        if not self._config.validate_site_name(self.site_name):
            logging.error("Failed to start the RedditScraper due to invalid praw.ini file")
            return
        self._reddit_api = reddit_api.RedditAPI(site_name=self.site_name)
        self._running = True
        self._start_retrieval_loop()

    def stop(self):
        """
        Stops the RedditScraper.
        :return:
        """
        self._running = False

    def _start_retrieval_loop(self):
        """
        Starts the retrieval loop for the RedditScraper.
        :return:
        """
        self._running = True
        followed_subreddits = self._get_followed_subreddit_list()
        while self._running:
            sleep(1)
            self._message_bus.publish(
                message_bus.Publish(
                    channel=Channel.RESEARCH,
                    message=Message(
                        header="reddit",
                        data_model="Hello World!"
                    )
                )
            )

    def _get_followed_subreddit_list(self):
        """
        Gets the list of subreddits that the RedditScraper is following.
        :return:
        """
        return self._reddit_api.user.subreddits(limit=None)

    @property
    def running(self):
        """
        Returns whether the RedditScraper is running.
        :return:
        """
        return self._running
