import os
import yaml
from . import stockbroker
from . import database


def validate_file(name, path=None):
    """
    Validate that a file exists.
    :param name: The name of the file.
    :param path: The path to the file.
    :return:
    """
    if path:
        file = os.path.join(path, name)
    else:
        file = name

    return os.path.exists(file)


def read_yaml_file(name, path=None):
    """
    Read a yaml file and return the contents as a dictionary.
    :param name: The name of the yaml file.
    :param path: The path to the yaml file. If not provided, the current working directory will be used.
    """
    if path:
        file = os.path.join(path, name)
    else:
        file = name

    if validate_file(name, path):
        with open(file, 'r') as stream:
            try:
                yaml_data = yaml.safe_load(stream)
                return yaml_data
            except yaml.YAMLError as exc:
                print(exc)
    else:
        raise FileNotFoundError('The file {} does not exist.'.format(name))


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

    raise FileNotFoundError('The file {} does not exist.'.format(name))


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
