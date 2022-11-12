from typing import TypeVar, List
from .models import docker_compose_command_model, docker_command_model
from .helpers import run_shell_command, run_asyncio_commands

T = TypeVar('T',
            docker_compose_command_model.DockerComposeCommandModel,
            docker_command_model.DockerCommandModel)


class CLI(object):
    def __init__(self):
        self.command_history: List[str] = []

    def run_command(self, command: T):
        if command.__name__() == 'DockerComposeCommandModel':
            command = command.cli_format()
            task = [run_shell_command(command)]
            run_asyncio_commands(task)
            self.command_history.append(command)
