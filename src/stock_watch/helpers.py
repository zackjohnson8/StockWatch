import sys
import yaml
import src.stock_watch.logger as logger
logging = logger.get(__name__)


def read_yaml_file(directory):
    with open(directory, 'r') as stream:
        try:
            yaml_data = yaml.safe_load(stream)
            return yaml_data
        except yaml.YAMLError as exc:
            print(exc)


def check_value(value):
    if value[0] == '<' and value[len(value) - 1] == '>':
        logging.error(f'Please update the value of {value} in the startup_config.yml file')
        sys.exit(1)
    return value
