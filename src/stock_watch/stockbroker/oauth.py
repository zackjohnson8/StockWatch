import requests

from src.stock_watch import logger
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel

logging = logger.get(__name__)


class OAuth:
    def __init__(self, stockbroker_credential: StockbrokerCredentialModel):
        """
        This object is used to handle authentication with the TD Ameritrade API.
        :param stockbroker_credential: Credentials to access the TD Ameritrade API.
        """
        self.stockbroker_credential = stockbroker_credential

    def _post_access_token(self) -> str:
        """
        This method is used to get an access token from the TD Ameritrade API. Using the get access token will handle
            this for you.
        :return: Access token.
        """
        if self.stockbroker_credential.access_token is None:
            response = requests.post(
                url='https://api.tdameritrade.com/v1/oauth2/token',
                data={
                    'grant_type': 'refresh_token',
                    'refresh_token': self.stockbroker_credential.refresh_token,
                    'client_id': self.stockbroker_credential.client_id,
                    'redirect_uri': self.stockbroker_credential.redirect_url
                }
            )
            if response.status_code == 200:
                self.stockbroker_credential.access_token = response.json()['access_token']
            else:
                return logger.error(f'Error: {response.status_code} {response.reason}')

        return self.stockbroker_credential.access_token

    def get_access_token(self) -> str:
        """
        This method is used to get an access token from the TD Ameritrade API.
        :return: Access token.
        """
        return self._post_access_token()
