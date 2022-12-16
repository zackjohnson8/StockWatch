from __future__ import absolute_import

# Packages
from . import data_scraper
from . import database
from . import docker
from . import stockbroker
from . import message_bus

# Files
from .helpers import read_yaml_file, find_file, get_stockbroker_configs, get_database_configs
from .logger import get, setup_logging
from .app import StockWatch
from .arguments import ArgumentParser
from .message_bus import MessageBus

__all__ = [docker, database, stockbroker, data_scraper, StockWatch, ArgumentParser, read_yaml_file, find_file,
           get_stockbroker_configs, get_database_configs, get, setup_logging, message_bus]

# Constants
try:
    STOCKBROKER_CREDENTIALS = get_stockbroker_configs()
    DATABASE_CREDENTIALS = get_database_configs()
except FileNotFoundError:
    STOCKBROKER_CREDENTIALS = None
    DATABASE_CREDENTIALS = None

try:
    logging_config_directory = helpers.find_file('logging_config.yml', './')
    logger.setup_logging(logging_config_directory)
except FileNotFoundError:
    print("Logging config file not found. Using default logging config.")
    logging_config = None

# Keep this at the bottom of the file. Logging breaks if this is moved. I don't know why.
message_bus = MessageBus.get_instance()
