import pytest
import os
import yaml

from src.stock_watch.helpers import read_yaml_file, validate_file


def test_validate_file():
    # Create a sample yaml file to read
    yaml_data = {'key1': 'value1', 'key2': 'value2'}
    with open('sample.yaml', 'w') as f:
        yaml.dump(yaml_data, f)

    # Test that the function correctly identifies a valid directory
    assert validate_file('sample.yaml') == True

    # Test that the function correctly identifies an invalid directory
    assert validate_file('invalid.yaml') == False

    os.remove('sample.yaml')


def test_read_yaml_file():
    # Create a sample yaml file to read
    yaml_data = {'key1': 'value1', 'key2': 'value2'}
    with open('sample.yaml', 'w') as f:
        yaml.dump(yaml_data, f)

    read_yaml_data = read_yaml_file('sample.yaml')
    assert read_yaml_data == yaml_data

    os.remove('sample.yaml')


def test_read_yaml_file_invalid_file():
    # Test that the function raises an error when given an invalid file path
    with pytest.raises(FileNotFoundError):
        read_yaml_file('invalid_file.yaml')
