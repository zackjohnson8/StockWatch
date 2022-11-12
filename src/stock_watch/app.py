import multiprocessing
import helpers
import docker
import data_scraper
import stockbroker


class StockWatch:

    def __init__(self):
        self.stockbroker_service = None
        self.ds_service = None

    def run(self):
        # Spin up the dockerized database
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        docker_compose_command = docker.DockerComposeCommandModel(
            command=docker.DockerComposeCommandType.UP,
            files=[docker_directory],
            child_options={'--build': None, '--force-recreate': None, '--detach': None}
        )
        docker_cli = docker.CLI()
        docker_cli.run_command(command=docker_compose_command)

        # Start the data scraper service. This will monitor a list of web sources for prudent information. This will
        # populate the database with data to be used by an Analysis Service.
        self.ds_service = data_scraper.DataScraperService()
        p1 = multiprocessing.Process(target=self.ds_service.run())
        p1.start()

        # TODO: Rework this service to reflect the addition of data_scraping. This
        #  service will probably only be used for trading and monitoring stocks that are actively being traded.
        stockbroker_credentials, database_credentials = helpers.get_startup_configs()
        self.stockbroker_service = stockbroker.StockbrokerService(
            stockbroker_credentials=stockbroker_credentials,
            database_credentials=database_credentials
        )
        p2 = multiprocessing.Process(target=lambda: self.stockbroker_service.run())
        p2.start()

        p1.join()
        p2.join()
