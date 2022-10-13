from build.lib.src.stock_watch.docker.helpers import command_helper
from src.stock_watch import logger
from src.stock_watch.stockbroker.docker.models import docker_command_model, docker_compose_command_model, \
    docker_credential_model
from src.stock_watch.stockbroker.docker.models.types import docker_command_type

logging = logger.get(__name__)


class DockerService:
    def __init__(self, docker_credentials: docker_credential_model.DockerCredentialModel):
        """
        :param docker_credentials DockerCredentialModel: The docker credential model for
            interacting with the docker service.
        """
        login_command_model = docker_command_model.DockerCommandModel(
            child_command=docker_command_type.DockerCommandType.LOGIN,
            child_input_command_options={'--username': docker_credentials.username,
                                         '--password': docker_credentials.password}
        )
        login_command = command_helper.create_docker_command(login_command_model)
        command_helper.run_commands(login_command)

    def execute(self, docker_compose_command: docker_compose_command_model.DockerComposeCommandModel):
        """
        Start the docker compose containers
        :param docker_compose_command:
        """
        command = command_helper.create_docker_compose_command(docker_compose_command=docker_compose_command)
        command_helper.run_commands(commands=command)
