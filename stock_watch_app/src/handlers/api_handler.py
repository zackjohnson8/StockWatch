import requests
from stock_watch_app.src.models.api_config import APIConfig

import stock_watch_app.src.extends.logger as logging

logger = logging.get_logger(__name__)


class ApiHandler:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config
        # Refresh the access token if it has expired
        if self.api_config.access_token is None:
            self.api_config.access_token = self.refresh_access_token()

    def refresh_access_token(self) -> str:
        response = requests.post(
            url='https://api.tdameritrade.com/v1/oauth2/token',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': self.api_config.refresh_token,
                'client_id': self.api_config.client_id,
                'redirect_uri': self.api_config.redirect_url
            }
        )
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            return logger.error(f'Error: {response.status_code} {response.reason}')

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
