from enum import Enum


class Program(Enum):
    """
    The enum selection of programs supported to run by the CLI.
    """
    DOCKER = 'docker'
    DOCKER_COMPOSE = 'docker-compose'
