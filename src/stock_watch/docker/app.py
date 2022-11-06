import asyncio

import src.stock_watch.docker.helpers as command_helper
from src.stock_watch.docker.models.command_model import CommandModel


class DockerCLI:
    def __init__(self):
        pass

    def run(self, docker_command: CommandModel):
        command = command_helper.create_docker_compose_command(docker_compose_command=docker_command)
        command_helper.run_commands(commands=command)


class ComposeCLI:
    def __init__(self):
        pass

    async def run(self, docker_compose_command: CommandModel):
        command = command_helper.create_docker_compose_command(docker_compose_command=docker_compose_command)
        command_helper.run_commands(commands=command)
        await asyncio.sleep(1)


class Docker:
    """
    This class is an entry point into this package.
    """
    def __init__(self):
        self.ComposeCLI = ComposeCLI()
