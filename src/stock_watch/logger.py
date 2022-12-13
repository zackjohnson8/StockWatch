import os
import yaml
import logging
import logging.config

DEFAULT_LEVEL = logging.INFO

# Create logs folder
if not os.path.exists('./src/stock_watch/logs'):
    os.makedirs('./src/stock_watch/logs')


def get(name):
    return logging.getLogger(name)


def setup_logging(config_path, default_level=DEFAULT_LEVEL):
    try:
        with open(config_path, 'rt') as cfg_file:
            config_file = yaml.safe_load(cfg_file.read())
            logging.config.dictConfig(config_file)
    except Exception as e:
        print(f'Error: {e}, with file, using Default logging')
        logging.basicConfig(level=default_level)
