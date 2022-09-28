import requests
from configs.api_config import APIConfig

import extends.logger as logging

logger = logging.get_logger(__name__)


class ApiHandler:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config

    def get(self, url, params=None):
        response = requests.get(url, params=params, headers={'Authorization': f'Bearer {self.api_config.access_token}'})
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')

    def post(self, url, data=None):
        response = requests.post(url, data=data, headers={'Authorization': f'Bearer {self.api_config.access_token}'})
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')

    def put(self, url, data=None):
        response = requests.put(url, data=data, headers={'Authorization': f'Bearer {self.api_config.access_token}'})
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')

    def delete(self, url, data=None):
        response = requests.delete(url, data=data, headers={'Authorization': f'Bearer {self.api_config.access_token}'})
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')
