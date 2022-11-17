import logging

from ..configs import config
from ..apis import reddit_api


class RedditScraper(object):
    """
    Praw Reddit API Decorator
    """

    def __init__(self):
        self._running = False
        self._config = config.Config()

        self._reddit_api = reddit_api.RedditAPI(config=self._config, site_name="stock_watch_bot")
        logging.info(self._reddit_api.user.me())

    def run(self):
        """
            - get updated list of subreddits
            - get new posts
                - parser?
                - hot, top, new, rising
            - store data in database
                - buffer, query, parser?
        """
        followed_subreddits = self._reddit_api.user.subreddits(limit=None)
        logging.info(f"Followed subreddits: {followed_subreddits}")
        self._running = True
        while self._running:
            pass

    def stop(self):
        self._running = False
