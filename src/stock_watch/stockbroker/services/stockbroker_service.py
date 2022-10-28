import time

from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel
from src.stock_watch.stockbroker.oauth import OAuth

import src.stock_watch.logger as logger

logging = logger.get(__name__)


class StockbrokerService:
    """
    This service retrieves data from the stockbroker api and stores it in the database.
    """

    def __init__(self, stockbroker_credential: StockbrokerCredentialModel):
        """
        :param stockbroker_credential: The credentials for accessing the stockbroker api.
        """
        self.oauth = OAuth(stockbroker_credential)

    def run(self):
        access_token = self.oauth.get_token()

        # Every 0.7 seconds request the api handler
        while True:
            logging.info("api_service: waiting on implementation")
            time.sleep(.7)
