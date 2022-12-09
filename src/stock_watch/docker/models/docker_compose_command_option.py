from enum import Enum


class DockerComposeCommandOption(Enum):
    """
    The enum selection of docker compose commands.
    """
    BUILD = 'build'
    CONVERT = 'convert'
    CP = 'cp'
    CREATE = 'create'
    DOWN = 'down'
    EVENTS = 'events'
    EXEC = 'exec'
    IMAGES = 'images'
    KILL = 'kill'
    LOGS = 'logs'
    LS = 'ls'
    PAUSE = 'pause'
    PORT = 'port'
    PS = 'ps'
    PULL = 'pull'
    RESTART = 'restart'
    RM = 'rm'
    RUN = 'run'
    START = 'start'
    STOP = 'stop'
    TOP = 'top'
    UNPAUSE = 'unpause'
    UP = 'up'
    VERSION = 'version'
