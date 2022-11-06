import asyncio
import multiprocessing

from src.stock_watch import flaskr, helpers
from src.stock_watch.docker.app import Docker
from src.stock_watch.docker.models.command_model import CommandModel
from src.stock_watch.docker.models.docker_credential_model import DockerCredentialModel
from src.stock_watch.docker.models.types.docker_compose_command_type import DockerComposeCommandType
from src.stock_watch.database.models.database_credential_model import DatabaseCredentialModel
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel
from src.stock_watch.stockbroker.services.stockbroker_service import StockbrokerService


class StockWatch:

    def __init__(self):
        self.stockbroker_service = None
        self.stockbroker_credentials = None
        self.database_credentials = None
        self.docker_credentials = None
        self.stockbroker = None

    def run(self):
        # Use helpers to retrieve credentials from the startup_configs
        startup_config = helpers.read_yaml_file('./src/stock_watch/configs/startup_config.yml')

        # TODO: Add logic to add the dockerhub username to the docker compose file
        self.docker_credentials = DockerCredentialModel(
            username=helpers.check_value(startup_config['dockerhub']['username']),
            password=helpers.check_value(startup_config['dockerhub']['password'])
        )

        self.stockbroker_credentials = StockbrokerCredentialModel(
            client_id=helpers.check_value(startup_config['stockbroker']['client_id']),
            redirect_url=helpers.check_value(startup_config['stockbroker']['redirect_uri']),
            refresh_token=helpers.check_value(startup_config['stockbroker']['refresh_token'])
        )

        # TODO: Fix the hard coded database credentials
        self.database_credentials = DatabaseCredentialModel(database_name='stockdata',
                                                            user='stockdata',
                                                            host='localhost',
                                                            password='mysecretpassword')

        # Spin up the dockerized database
        docker_directory = f'src/stock_watch/docker/configs/docker_compose/docker-compose-database.yml'
        docker_compose_command = CommandModel(
            child_command=DockerComposeCommandType.UP,
            child_command_options=['--build', '--force-recreate', '--detach'],
            parent_input_options={'-f': docker_directory},
        )
        asyncio.run(Docker().ComposeCLI.run(docker_compose_command=docker_compose_command))

        self.stockbroker_service = StockbrokerService(
            stockbroker_credentials=self.stockbroker_credentials,
            database_credentials=self.database_credentials
        )

        p = multiprocessing.Process(target=lambda: flaskr.run())
        p.start()

        p2 = multiprocessing.Process(target=lambda: self.stockbroker_service.run())
        p2.start()

        p.join()
        p2.join()
