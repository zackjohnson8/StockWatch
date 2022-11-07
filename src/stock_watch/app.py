import multiprocessing
import time

from src.stock_watch import flaskr, helpers
from src.stock_watch.docker.app import Docker
from src.stock_watch.docker.models.command_model import CommandModel
from src.stock_watch.docker.models.types.docker_compose_command_type import DockerComposeCommandType
from src.stock_watch.helpers import get_startup_configs
from src.stock_watch.stockbroker.services.stockbroker_service import StockbrokerService


class StockWatch:

    def __init__(self):
        self.stockbroker_service = None
        self.stockbroker_credentials = None
        self.database_credentials = None
        self.docker_credentials = None
        self.stockbroker = None

    def run(self):
        # Spin up the dockerized database
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        docker_compose_command = CommandModel(
            child_command=DockerComposeCommandType.UP,
            child_command_options=['--build', '--force-recreate', '--detach'],
            parent_input_options={'-f': docker_directory},
        )
        Docker().ComposeCLI.run(docker_compose_command=docker_compose_command)

        # TODO: This needs to be implemented with the nginx server. Currently, this is running locally.
        p = multiprocessing.Process(target=lambda: flaskr.run())
        p.start()

        # TODO: Using this to slow down the program so that the database can be created. Something needs to be
        #  changed either in the Docker() or checked for in the StockBrokerService()
        time.sleep(5)

        # Get the startup configs from the startup_config file in the config folder. Be sure to modify this file before
        # running the application.
        stockbroker_credentials, database_credentials = get_startup_configs()
        # Spin up the stockbroker service
        self.stockbroker_service = StockbrokerService(
            stockbroker_credentials=stockbroker_credentials,
            database_credentials=database_credentials
        )
        p2 = multiprocessing.Process(target=lambda: self.stockbroker_service.run())
        p2.start()

        p.join()
        p2.join()
