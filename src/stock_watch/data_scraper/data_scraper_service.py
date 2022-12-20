from .scrapers.scraper import Scraper
from .scraper_process import ScraperProcess
from .process_manager import ProcessManager


class DataScraperService(object):

    def __init__(self):
        """
        The DataScraperService class is used to manage a list of scrapers. Each scraper will retrieve data from
        whichever source it is designed to retrieve data from.
        """
        self.process_manager = ProcessManager()
        self.scraper_list = []

    def add_scraper(self, scraper: Scraper):
        """
        Add a scraper that DataScraperService will manage
        :param scraper: A scraper object to be managed by the DataScraperService
        :return:
        """
        # Add scraper to the scraper list
        self.scraper_list.append(scraper)
        # Each scraper will have a process associated with it and added to the process manager
        s_process = ScraperProcess(scraper=scraper)
        self.process_manager.add_process(process=s_process)

    def start_scrapers(self):
        """
        Start all the scrapers that have been added to the DataScraperService
        :return:
        """
        # Each scraper that was added to this class has a corresponding process created. Start all the processes in the
        # process manager.
        self.process_manager.start_all_processes()

    def stop_scrapers(self):
        self.process_manager.stop_all_processes()

    def has_scraper(self, scraper: Scraper) -> bool:
        """
        Check if a scraper was added to the DataScraperService
        :param scraper: The scraper to check
        :return: True if the scraper is in the scraper list, False otherwise
        """
        for list_scraper in self.scraper_list:
            if list_scraper == scraper:
                return True
        return False
