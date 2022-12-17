import pytest
import src.stock_watch.data_scraper as data_scraper
import src.stock_watch.data_scraper.scrapers as scrapers

def test_CreateARedditScraperWithoutChangingPrawIniFile_InformUserItNeedsToBeUpdated():
    # Create data scraper service
    data_scraper_service = data_scraper.data_scraper_service.DataScraperService()

    # Create custom config
    custom_config = data_scraper.configs.config.Config(praw_file_dir="tests/test_data_scraper/praw.ini")

    # Add a reddit scraper to the data scraper service
    reddit_scraper = scrapers.reddit_scraper.RedditScraper(config=custom_config)

    # Add the reddit scraper to the data scraper service
    data_scraper_service.add_scraper(scraper=reddit_scraper)

    # Check that the data scraper service has the reddit scraper
    assert data_scraper_service.has_scraper(scraper=reddit_scraper) == True
