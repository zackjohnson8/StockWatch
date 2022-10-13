import subprocess
import src.stock_watch.logger as logger
from src.stock_watch.stockbroker.docker.models.docker_command_model import DockerCommandModel
from src.stock_watch.stockbroker.docker.models.docker_compose_command_model import DockerComposeCommandModel

logging = logger.get(__name__)


def run_commands(commands: list, wait: bool = True) -> str:
    popen = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
    if wait:
        popen.wait()
    stdout, stderr = popen.communicate()
    if stderr:
        logging.info(f'{stderr}: stdout: {stdout}')
    else:
        logging.info(stdout)
        return stdout


def create_docker_command(docker_command: DockerCommandModel) -> list[str]:
    """
    Create the docker command
    :param docker_command:
    """
    command = ['docker']

    if docker_command.parent_options:
        command = [*command, *docker_command.parent_options]

    if docker_command.parent_input_options:
        for key, value in docker_command.parent_input_options.items():
            if value:
                command = [*command, key, value]

    command = [*command, docker_command.child_command.value]

    if docker_command.child_command_options:
        command = [*command, *docker_command.child_command_options]

    if docker_command.child_input_command_options:
        for key, value in docker_command.child_input_command_options.items():
            if value:
                command = [*command, key, value]

    return command


def create_docker_compose_command(docker_compose_command: DockerComposeCommandModel) -> list[str]:
    """
    Create the docker compose command
    :param docker_compose_command:
    """
    command = ['docker-compose']

    if docker_compose_command.parent_options:
        command = [*command, *docker_compose_command.parent_options]

    if docker_compose_command.parent_input_options:
        for key, value in docker_compose_command.parent_input_options.items():
            if value:
                command = [*command, key, value]

    command = [*command, docker_compose_command.child_command.value]

    if docker_compose_command.child_command_options:
        command = [*command, *docker_compose_command.child_command_options]

    if docker_compose_command.child_input_command_options:
        for key, value in docker_compose_command.child_input_command_options.items():
            if value:
                command = [*command, key, value]

    return command
