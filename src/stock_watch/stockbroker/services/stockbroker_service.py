import time
from datetime import datetime, timezone, timedelta


from src.stock_watch.database.database import Database
from src.stock_watch.database.models.database_credential_model import DatabaseCredentialModel
from src.stock_watch.stockbroker.api import movers
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel
from src.stock_watch.stockbroker.models.types.direction_type import DirectionType
from src.stock_watch.stockbroker.models.types.stock_index_type import StockIndexType
from src.stock_watch.stockbroker.models.types.value_change_type import ValueChangeType
from src.stock_watch.stockbroker.oauth import OAuth

import src.stock_watch.logger as logger

logging = logger.get(__name__)


class StockbrokerService:
    """
    This service retrieves data from the stockbroker api and stores it in the database.
    """

    def __init__(self,
                 stockbroker_credentials: StockbrokerCredentialModel,
                 database_credentials: DatabaseCredentialModel
                 ):
        """
        :param stockbroker_credential: The credentials for accessing the stockbroker api.
        :param database_credential: The credentials for accessing the database service.
        """
        self.oauth = OAuth(stockbroker_credentials)
        self.db = Database(database_credentials=database_credentials)

    def run(self):
        direction_change = True
        eastern = timezone(offset=timedelta(hours=-4))
        while True:
            current_weekday = datetime.today().weekday()
            current_time = datetime.now(tz=eastern).time()
            open_time = datetime.strptime('09:30:00', '%H:%M:%S').time()
            close_time = datetime.strptime('16:00:00', '%H:%M:%S').time()

            # Only run this logic on weekdays
            if current_weekday < 5 and open_time < current_time < close_time:
                if direction_change:
                    up_movers = movers.get(oauth=self.oauth, index=StockIndexType.NASDAQ, direction=DirectionType.UP,
                                            change=ValueChangeType.PERCENT)
                else:
                    down_movers = movers.get(oauth=self.oauth, index=StockIndexType.NASDAQ, direction=DirectionType.DOWN,
                                            change=ValueChangeType.PERCENT)
                direction_change = not direction_change
            else:
                logging.info('Sleeping until tomorrow')

            time.sleep(.6)
