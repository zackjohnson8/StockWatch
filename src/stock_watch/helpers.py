import os
import sys
import yaml
import database
import stockbroker

import logger
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


def get_startup_configs():
    startup_config = read_yaml_file(find_file('startup_config.yml', './'))

    return stockbroker.models.StockbrokerCredentialModel(
        client_id=check_value(startup_config['stockbroker']['client_id']),
        redirect_url=check_value(startup_config['stockbroker']['redirect_uri']),
        refresh_token=check_value(startup_config['stockbroker']['refresh_token'])
    ), database.models.DatabaseCredentialModel(
        database_name=check_value(startup_config['database']['name']),
        user=check_value(startup_config['database']['user']),
        host=check_value(startup_config['database']['host']),
        password=check_value(startup_config['database']['password'])
    )


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def get_stock_list_from_csv(file_name):
    file = find_file(file_name, './')
    stock_list = []
    with open(file, 'r') as file:
        for line in file:
            symbol = line[:line.find(',')]
            stock_list.append(symbol)
    return stock_list
