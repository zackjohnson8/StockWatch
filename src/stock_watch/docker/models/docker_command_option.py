from enum import Enum


class DockerCommandOption(Enum):
    """
    The enum selection of docker commands.
    """
    LOGIN = 'login'
    LOGOUT = 'logout'
