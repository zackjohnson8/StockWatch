import os
import yaml
from . import stockbroker
from . import database


def read_yaml_file(directory):
    """
    Read a yaml file and return the contents as a dictionary.
    :param directory: The directory of the yaml file to be read.
    :return:
    """
    with open(directory, 'r') as stream:
        try:
            yaml_data = yaml.safe_load(stream)
            return yaml_data
        except yaml.YAMLError as exc:
            print(exc)


def find_file(name, path):
    """
    Find a file in a directory.
    :param name: File name
    :param path: Path to directory
    :return:
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def get_stockbroker_configs():
    """
    Get the stockbroker configs from the startup_config.yml file.
    :return:
    """
    config = read_yaml_file(find_file('startup_config.yml', './'))
    return stockbroker.models.StockbrokerCredentialModel(
        client_id=config['stockbroker']['client_id'],
        redirect_url=config['stockbroker']['redirect_uri'],
        refresh_token=config['stockbroker']['refresh_token']
    )


def get_database_configs():
    """
    Get the database configs from the startup_config.yml file.
    :return:
    """
    config = read_yaml_file(find_file('startup_config.yml', './'))
    return database.models.DatabaseCredentialModel(
        database_name=config['database']['name'],
        user=config['database']['user'],
        host=config['database']['host'],
        password=config['database']['password']
    )


def get_stock_list_from_csv(file_name):
    """
    Get a list of stocks from a csv file.
    :param file_name: The name of the csv file.
    :return:
    """
    file = find_file(file_name, './')
    stock_list = []
    with open(file, 'r') as file:
        for line in file:
            symbol = line[:line.find(',')]
            stock_list.append(symbol)
    return stock_list
