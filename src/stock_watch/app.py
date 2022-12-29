import multiprocessing

from . import helpers
from . import docker
from . import data_scraper
import logging
import src.stock_watch as stock_watch
import sys
from src.stock_watch.gui.main_window import MainWindow
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.subscription import Subscription
from src.stock_watch.gui.application import Application

class StockWatch:

    def __init__(self):
        self._message_bus = None
        self.data_scraper_service = None
        self.stockbroker_service = None
        self.main_window = None

    def run(self):
        logging.info('Starting StockWatch')
        # Start the message bus
        self._message_bus = stock_watch.message_bus.get_instance()

        # Docker
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        docker_compose_command = docker.models.DockerComposeCommand(
            command=docker.models.DockerComposeCommandOption.UP,
            files=[docker_directory],
            child_options={'--build': None, '--force-recreate': None, '--detach': None}
        )
        docker_cli = docker.CLI()
        docker_cli.run_command(command=docker_compose_command)

        # Data Scraping
        # Create a scraper service to manage the scrapers
        self.data_scraper_service = data_scraper.DataScraperService()
        # Create scrapers
        reddit_scraper = data_scraper.scrapers.reddit_scraper.RedditScraper()
        if reddit_scraper.validate_praw_ini_updated():
            # Add scrapers to the scraper service
            self.data_scraper_service.add_scraper(scraper=reddit_scraper)
            # Start scraper service
            scaper_parent_conn, child_conn = multiprocessing.Pipe(duplex=True)
            data_scraper_process = multiprocessing.Process(target=self.data_scraper_service.start_scrapers,
                                                           args=(child_conn,))
            data_scraper_process.start()

        # Subscribe to receive messages from the message bus
        # Add subscriptions to the message bus here then start the message bus
        self._message_bus.start()

        app = Application(sys.argv)
        self.main_window = MainWindow()
        app.exec()

        # Stop all services
        self._message_bus.stop()
        self.data_scraper_service.stop_scrapers()
