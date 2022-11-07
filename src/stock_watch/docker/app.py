import asyncio

import src.stock_watch.docker.helpers as command_helper
from src.stock_watch.docker.models.command_model import CommandModel


class DockerCLI:
    def __init__(self):
        pass

    def run(self, docker_command: CommandModel):
        command = command_helper.create_command(commands=docker_command)
        task = [command_helper.run_command(*command)]
        command_helper.run_asyncio_commands(task)


class ComposeCLI:
    def __init__(self):
        pass

    def run(self, docker_compose_command: CommandModel):
        command = command_helper.create_command(commands=docker_compose_command)
        task = [command_helper.run_command(*command)]
        command_helper.run_asyncio_commands(task)


class Docker:
    """
    This class is an entry point into this package.
    """
    def __init__(self):
        self.ComposeCLI = ComposeCLI()
