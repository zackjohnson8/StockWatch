import logging
from typing import TypeVar, List
from .models import docker_compose_command, docker_command
from .helpers import run_shell_command, run_asyncio_commands

T = TypeVar('T',
            docker_compose_command.DockerComposeCommand,
            docker_command.DockerCommand)

class CLI(object):
    def __init__(self):
        self.command_history: List[str] = []

    def run_command(self, command: T):
        """
        Run a docker command
        :param command: a docker command model such as DockerComposeCommandModel or DockerCommandModel
        :return:
        """
        logging.info(f'Running command: {command}')
        if command.__name__() == 'DockerComposeCommand':
            command = command.cli_format()
            task = [run_shell_command(command)]
            run_asyncio_commands(task)
            self.command_history.append(command)
