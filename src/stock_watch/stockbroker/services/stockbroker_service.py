import time

from src.stock_watch.stockbroker.database.database import Database
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel
from src.stock_watch.stockbroker.models.types.direction_type import DirectionType
from src.stock_watch.stockbroker.models.types.stock_index_type import StockIndexType
from src.stock_watch.stockbroker.models.types.value_change_type import ValueChangeType
from src.stock_watch.stockbroker.oauth import OAuth
import src.stock_watch.stockbroker.api.movers as movers

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
        self.db = Database()

    def run(self):
        direction_change = True
        while True:


            if direction_change:
                up_movers = movers.get(oauth=self.oauth, index=StockIndexType.NASDAQ, direction=DirectionType.UP,
                                        change=ValueChangeType.PERCENT)
                pass
            else:
                down_movers = movers.get(oauth=self.oauth, index=StockIndexType.NASDAQ, direction=DirectionType.DOWN,
                                        change=ValueChangeType.PERCENT)
                pass
            direction_change != direction_change
            time.sleep(.6)
