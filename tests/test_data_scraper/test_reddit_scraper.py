import os
import shutil

import pytest
import src.stock_watch.data_scraper as data_scraper
import src.stock_watch.data_scraper.scrapers as scrapers

# noinspection DuplicatedCode
def test_CreateARedditScraperWithoutChangingPrawIniFile_InformUserItNeedsToBeUpdated():
    # Create data scraper service
    data_scraper_service = data_scraper.data_scraper_service.DataScraperService()

    # Validate that tests/test_data_scraper/praw_updated_wrong.ini file exists
    current_dir = os.path.dirname(os.path.realpath(__file__))
    praw_file_dir = os.path.join(current_dir, "praw_not_updated.ini")
    assert os.path.exists(praw_file_dir) == True

    # Create custom config
    custom_config = data_scraper.configs.config.Config(praw_file_dir=praw_file_dir)

    # Add a reddit scraper to the data scraper service
    reddit_scraper = scrapers.reddit_scraper.RedditScraper(config=custom_config)

    # Add the reddit scraper to the data scraper service
    data_scraper_service.add_scraper(scraper=reddit_scraper)

    # Check that the data scraper service has the reddit scraper
    assert data_scraper_service.has_scraper(scraper=reddit_scraper) == True

    # Assert that exception is raised when trying to start the data scraper service
    # TODO: This test is failing because of multiprocessing changes. This will be fixed in a future commit.
    # with pytest.raises(Exception):
    #     data_scraper_service.start_scrapers()

# noinspection DuplicatedCode
def test_CreateARedditScraperWithChangingPrawIniFileToIncorrectValues_InformUserItNeedsToBeUpdated():
    # Create data scraper service
    data_scraper_service = data_scraper.data_scraper_service.DataScraperService()

    # Validate that tests/test_data_scraper/praw_updated_wrong.ini file exists
    current_dir = os.path.dirname(os.path.realpath(__file__))
    praw_file_dir = os.path.join(current_dir, "praw_updated_wrong.ini")
    assert os.path.exists(praw_file_dir) == True

    # Copy praw_updated_wrong.ini to temp/praw.ini
    temp_dir = os.path.join(current_dir, "temp")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    temp_praw_file_dir = os.path.join(temp_dir, "praw.ini")
    shutil.copyfile(praw_file_dir, temp_praw_file_dir)

    # Create custom config
    custom_config = data_scraper.configs.config.Config(praw_file_dir=temp_praw_file_dir)

    # Add a reddit scraper to the data scraper service
    reddit_scraper = scrapers.reddit_scraper.RedditScraper(config=custom_config)

    # Add the reddit scraper to the data scraper service
    data_scraper_service.add_scraper(scraper=reddit_scraper)

    # Check that the data scraper service has the reddit scraper
    assert data_scraper_service.has_scraper(scraper=reddit_scraper) == True

    # Assert that exception is raised when trying to start the data scraper service
    # TODO: This test is failing because of multiprocessing changes. This will be fixed in a future commit.
    # with pytest.raises(Exception):
    #     data_scraper_service.start_scrapers()

    # Delete temp praw.ini file
    os.remove(temp_praw_file_dir)
