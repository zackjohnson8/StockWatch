import logging
from time import sleep
from .scraper import Scraper
from ..apis import reddit_api


class RedditScraper(Scraper):
    def __init__(self):
        self._running = False
        self._reddit_api = reddit_api.RedditAPI(site_name="stock_watch_bot")
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
            logging.info(f"Followed subreddits: {followed_subreddits}")

    def _get_followed_subreddit_list(self):
        return self._reddit_api.user.subreddits(limit=None)

    @property
    def running(self):
        return self._running
