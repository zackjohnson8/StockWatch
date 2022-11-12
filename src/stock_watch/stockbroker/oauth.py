import requests
from datetime import datetime
from .models import StockbrokerCredentialModel


class OAuth:

    def __init__(self, stockbroker_credential: StockbrokerCredentialModel):
        """
        This object is used to handle authentication with the TD Ameritrade API.
        :param stockbroker_credential: Credentials to access the TD Ameritrade API.
        """
        self.access_token_refresh_time = None
        self.stockbroker_credential = stockbroker_credential

    def _get_access_token(self) -> str:
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
            self._update_access_token_refresh_time()
        else:
            # return logging.error(f'Error: {response.status_code} {response.reason}')
            pass

    def _update_access_token_refresh_time(self):
        self.access_token_refresh_time = datetime.now()

    def is_access_token_expired(self) -> bool:
        time_difference = datetime.now() - self.access_token_refresh_time
        if time_difference.seconds > 1790:
            return True
        return False

    def get_token(self) -> str:
        """
        This method is used to get an access token from the TD Ameritrade API.
        :return: Access token.
        """
        if self.stockbroker_credential.access_token is None:
            self._get_access_token()
        elif self.is_access_token_expired():
            self._get_access_token()

        return self.stockbroker_credential.access_token
