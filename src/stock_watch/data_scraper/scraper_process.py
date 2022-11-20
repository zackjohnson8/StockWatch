from .scrapers.scraper import Scraper
import multiprocessing
import logging


class ScraperProcess(object):
    def __init__(self, scraper: Scraper):
        """
        The ScraperProcess class is a wrapper around a scraper object to allow the scraper to be run in a separate
        process.
        :param scraper:
        """
        self._scraper = scraper
        self._running = False
        self._process = None

    def start(self):
        """
        Start the scraper in a separate process
        :return:
        """
        self._running = True
        self._process = multiprocessing.Process(target=lambda: self._scraper.start())
        self._process.start()
        logging.info(f"Started {self._scraper.__class__.__name__}")

    def stop(self):
        """
        Stop the scraper process
        :return:
        """
        self._running = False
        self._process.terminate()
        logging.info(f"Stopped {self._scraper.__class__.__name__}")

    @property
    def running(self):
        """
        Return whether the scraper process is running
        :return:
        """
        return self._running
