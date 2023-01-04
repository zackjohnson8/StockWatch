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
        self.parent_conn = None
        self.child_conn = None
        self._scraper = scraper
        self._running = False
        self._process = None

    def start(self) -> multiprocessing.connection.Connection:
        """
        Start the scraper in a separate process
        :return:
        """
        self._running = True
        self.parent_conn, self.child_conn = multiprocessing.Pipe(duplex=True)
        self._process = multiprocessing.Process(target=self._scraper.start, args=(self.child_conn,))
        self._process.start()
        logging.info(f"Started {self._scraper.__class__.__name__}")

        return self.parent_conn

    def stop(self):
        """
        Stop the scraper process
        :return:
        """
        if self._running:
            self._running = False
            self._process.terminate()
            self._process.join()
            logging.info(f"Stopped {self._scraper.__class__.__name__}")
        else:
            logging.warning(f"{self._scraper.__class__.__name__} is not running")

    @property
    def running(self):
        """
        Return whether the scraper process is running
        :return:
        """
        return self._running
