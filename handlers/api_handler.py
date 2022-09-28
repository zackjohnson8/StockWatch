import requests
from configs.api_config import APIConfig

import extends.logger as logging

logger = logging.get_logger(__name__)


class ApiHandler:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config

    def get(self, url, params=None, **kwargs):
        response = requests.get(
            url,
            params=params,
            headers={'Authorization': f'Bearer {self.api_config.access_token}'},
            **kwargs
        )
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')

    def post(self, url, data=None, json=None, **kwargs):
        response = requests.post(
            url,
            data=data,
            json=json,
            headers={'Authorization': f'Bearer {self.api_config.access_token}'},
            **kwargs
        )
        if response.status_code == 200:
            return response.json()
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')