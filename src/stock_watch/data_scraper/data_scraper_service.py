import multiprocessing

from .web_scrapers import reddit_scraper


class DataScraperService:
    def __init__(self):
        self.reddit_scraper = None
        self._reddit_scraper_process = None

    def start_scrapers(self):
        self.reddit_scraper = reddit_scraper.RedditScraper()
        self._reddit_scraper_process = multiprocessing.Process(target=lambda: self.reddit_scraper.run())
        self._reddit_scraper_process.start()
        self._reddit_scraper_process.join()
