import json
import time

from . import helpers
from . import docker
from . import data_scraper
import logging
import src.stock_watch as stock_watch
from src.stock_watch.message_bus.models.channel import Channel
from src.stock_watch.message_bus.models.subscription import Subscription


class StockWatch:

    def __init__(self):
        self._message_bus = None
        self.data_scraper_service = None
        self.stockbroker_service = None
        self.ds_service = None

    def run(self):
        logging.info('Starting StockWatch')
        # Start the message bus
        self._message_bus = stock_watch.message_bus.get_instance()
        self._message_bus.start()

        # Subscribe to all message types for testing.
        subscriptions = [Subscription(Channel.RESEARCH, self.on_research_message),
                         Subscription(Channel.TRADING, self.on_trading_message),
                         Subscription(Channel.ANALYSIS, self.on_analysis_message),
                         Subscription(Channel.DATABASE, self.on_database_message)]
        self._message_bus.subscribe(subscriptions)

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
        # Add scrapers to the scraper service
        self.data_scraper_service.add_scraper(scraper=reddit_scraper)
        # Start scraper service
        self.data_scraper_service.start_scrapers()

        # Stockbroker
        # TODO: Rework this service to reflect the addition of data_scraping. This
        #  service will probably only be used for trading and monitoring stocks that are actively being traded.
        # from stock_watch import STOCKBROKER_CREDENTIALS, DATABASE_CREDENTIALS
        # self.stockbroker_service = stockbroker.services.StockbrokerService(
        #     stockbroker_credentials=STOCKBROKER_CREDENTIALS,
        #     database_credentials=DATABASE_CREDENTIALS
        # )
        # stock_watch_process = multiprocessing.Process(target=lambda: self.stockbroker_service.run())
        # stock_watch_process.start()
        # logging.info('Started stock watch service')

        while True:
            time.sleep(1)

    # noinspection PyMethodMayBeStatic
    def on_research_message(self, message):
        message_dict = json.loads(message.data_model)
        logging.info('Received research message: {author} posted {title} from {url}'.format(
            author=message_dict['name'],
            title=message_dict['title'],
            url=message_dict['url']))

    # noinspection PyMethodMayBeStatic
    def on_analysis_message(self, message):
        logging.info('Received analysis message: {}'.format(message))

    # noinspection PyMethodMayBeStatic
    def on_trading_message(self, message):
        logging.info('Received trading message: {}'.format(message))

    # noinspection PyMethodMayBeStatic
    def on_database_message(self, message):
        logging.info('Received database message: {}'.format(message))
