import psycopg2

from src.stock_watch.stockbroker.docker.models import docker_credential_model
from src.stock_watch.stockbroker.docker.models import docker_compose_command_model
from src.stock_watch.stockbroker.docker.models.types import docker_compose_command_type
from src.stock_watch.stockbroker.docker.services import docker_service


class DatabaseService:
    def __init__(self, docker_credentials: docker_credential_model.DockerCredentialModel):
        self.service__ = """
        :param DockerCredentialModel docker_credentials: The docker credential model for
            interacting with the docker service.
        """
        self.docker_service = docker_service.DockerService(docker_credentials=docker_credentials)
        self.db = None

    def run(self):
        docker_directory = f'src/stock_watch/stockbroker/docker/configs/docker_compose/docker-compose-database.yml'
        # Start/Create a database using docker
        # Create a docker compose command model to pass into start
        docker_compose_command = docker_compose_command_model.DockerComposeCommandModel(
            child_command=docker_compose_command_type.DockerComposeCommandType.UP,
            child_command_options=['--build', '--force-recreate', '--detach'],
            parent_input_options={'-f': docker_directory},
        )
        self.docker_service.execute(docker_compose_command=docker_compose_command)

