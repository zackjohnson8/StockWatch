import logging
from time import sleep
from .scraper import Scraper
from ..apis import reddit_api
from ..configs.config import Config
import src.stock_watch as stock_watch
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.message import Message
from src.stock_watch.message_bus.models.publish import Publish
from src.stock_watch.message_bus.data_models.reddit.reddit_submission import RedditSubmission


class RedditScraper(Scraper):

    def __init__(self):
        """
        The RedditScraper is a scraper that scrapes data from Reddit. This uses the Reddit API provided from PRAW.
        """
        self._config = Config()
        self._running = False
        self._reddit_api = None
        self._message_bus = None
        self.site_name = "stock_watch_bot"

    def start(self):
        """
        Starts the RedditScraper. Cannot start without updating the praw.ini file with the correct credentials.
        :return:
        """
        if self._message_bus is None:
            self._message_bus = stock_watch.message_bus.get_instance()

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
        posts_retrieved_list = []
        while self._running:
            sleep(5)
            followed_subreddits = self._get_followed_subreddit_list()
            for subreddit in followed_subreddits:
                new_submissions = subreddit.new(limit=10)
                for submission in new_submissions:
                    if submission.name not in posts_retrieved_list:
                        reddit_post_data = RedditSubmission(reddit=self._reddit_api, submission_id=submission.id)
                        message = Message(
                            header="reddit_submission",
                            data_model=reddit_post_data.to_json()
                        )
                        self._message_bus.publish(Publish(channel=Channel.RESEARCH, message=message))
                        posts_retrieved_list.append(submission.name)
            # Remove any old posts from the posts_retrieved_list after 1000
            while len(posts_retrieved_list) > 1000:
                posts_retrieved_list.pop(0)

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
