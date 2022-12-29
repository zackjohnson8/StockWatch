import logging
from time import sleep
from .scraper import Scraper
from ..apis import reddit_api
from ..configs.config import Config
from typing import Optional
import src.stock_watch as stock_watch
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.message import Message
from src.stock_watch.message_bus.models.publish import Publish
from src.stock_watch.message_bus.data_models.reddit.reddit_submission import RedditSubmission


class RedditScraper(Scraper):

    def __init__(self, config: Optional[Config] = None):
        """
        The RedditScraper is a scraper that scrapes data from Reddit. This uses the Reddit API provided from PRAW.
        """
        if config is None:
            self.config = Config()
        else:
            self.config = config
        self._running = False
        self._reddit_api = None
        self._message_bus = stock_watch.message_bus.get_instance()
        self.site_name = "stock_watch_bot"


    def validate_praw_ini_updated(self) -> bool:
        """
        Validates that the praw.ini file has been updated with the correct credentials.
        :return: True if the praw.ini file has been updated with the correct credentials, False otherwise.
        """
        # Validate that the praw.ini has site_name and the required fields
        if not self.config.validate_site_name(self.site_name) or not self.config.validate_site_fields(self.site_name):
            logging.info("The praw.ini file is not configured correctly. Please update the praw.ini file with valid "
                         "site_name and required fields.")
            return False
        return True

    def start(self, conn):
        """
        Starts the RedditScraper. Cannot start without updating the praw.ini file with the correct credentials.
        :return:
        """
        if not self.validate_praw_ini_updated():
            raise Exception("The praw.ini file is not configured correctly. Please update the praw.ini file with valid "
                            "site_name and required fields. Call validate_praw_ini_updated() to check if the praw.ini "
                            "file is configured correctly.")
        self._reddit_api = reddit_api.RedditAPI(site_name=self.site_name, custom_config=self.config)
        self._start_retrieval_loop(conn)

    def stop(self):
        """
        Stops the RedditScraper.
        :return:
        """
        self._running = False

    def _start_retrieval_loop(self, conn):
        """
        Starts the retrieval loop for the RedditScraper.
        :return:
        """
        logging.info("Starting the retrieval loop for the RedditScraper...")
        self._running = True
        posts_retrieved_list = []
        while self._running:
            sleep(5)
            # Check conn for messages
            if conn.poll():
                logging.info("Received message") # template code for now

            # Check Reddit for new posts
            followed_subreddits = self._get_followed_subreddit_list()
            for subreddit in followed_subreddits:
                new_submissions = subreddit.new(limit=10)
                for submission in new_submissions:
                    if submission.name not in posts_retrieved_list:
                        reddit_post_data = RedditSubmission(reddit=self._reddit_api, submission_id=submission.id)
                        message = Message(
                            header="reddit_submission",
                            data_model=reddit_post_data.to_dict()
                        )
                        publish = Publish(channel=Channel.RESEARCH, message=message)
                        conn.send(publish)
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
