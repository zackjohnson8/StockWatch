import os

import yaml


def read_file(directory):
    if os.path.exists(directory):
        with open(directory, 'r') as stream:
            try:
                yaml_data = yaml.safe_load(stream)
                return yaml_data
            except yaml.YAMLError as exc:
                print(exc)
