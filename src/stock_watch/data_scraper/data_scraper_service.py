from .web_scrapers import reddit_scraper


class DataScraperService:
    def __init__(self):
        # Initializing Reddit using the praw.ini file. Be sure to input your credentials into the [stock_watch_bot].
        self.reddit_scraper = reddit_scraper.RedditScraper()

    def start_scrapers(self):
        self.reddit_scraper.run()

