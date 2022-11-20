import multiprocessing
import helpers
import docker
import data_scraper
import stockbroker
import logging


class StockWatch:

    def __init__(self):
        self.data_scraper_service = None
        self.stockbroker_service = None
        self.ds_service = None

    def run(self):
        logging.info('Starting StockWatch')

        # Docker
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        docker_compose_command = docker.models.DockerComposeCommandModel(
            command=docker.models.DockerComposeCommandType.UP,
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
        from stock_watch import STOCKBROKER_CREDENTIALS, DATABASE_CREDENTIALS
        self.stockbroker_service = stockbroker.services.StockbrokerService(
            stockbroker_credentials=STOCKBROKER_CREDENTIALS,
            database_credentials=DATABASE_CREDENTIALS
        )
        stock_watch_process = multiprocessing.Process(target=lambda: self.stockbroker_service.run())
        stock_watch_process.start()
        logging.info('Started stock watch service')

        # Join the services back
        logging.info('StockWatch has stopped')
