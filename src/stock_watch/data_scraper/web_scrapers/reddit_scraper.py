import os
import shutil
from sys import platform
import logging
import praw
import src.stock_watch.helpers as helpers


class RedditScraper(object):

    def __init__(self):
        self._running = False

        self._setup_praw_init_file()

        try:
            self._reddit_api = praw.Reddit(site_name="stock_watch_bot")
            logging.info(f"Reddit API initialized: {self._reddit_api.user.me()}")
        except Exception as e:
            logging.error(e)
            raise e

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

    def _setup_praw_init_file(self):
        if platform == "linux":
            praw_file_dir = helpers.find_file("praw.ini", "./")
            home_dir = os.getenv("HOME") + "/.config" + "/praw.ini"
            shutil.copyfile(praw_file_dir, home_dir)
