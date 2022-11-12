import asyncio
import time
from datetime import datetime

from src.stock_watch import helpers
from src.stock_watch.database.database_manager import DatabaseManager
from src.stock_watch.database.models.database_credential_model import DatabaseCredentialModel
from src.stock_watch.stockbroker.api import price_history
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel
from src.stock_watch.stockbroker.oauth import OAuth


class StockbrokerService:
    """
    This service retrieves data from the stockbroker api and stores it in the database.
    """

    def __init__(self,
                 stockbroker_credentials: StockbrokerCredentialModel,
                 database_credentials: DatabaseCredentialModel
                 ):
        """
        :param stockbroker_credentials: The credentials for accessing the stockbroker api.
        :param database_credentials: The credentials for accessing the database service.
        """
        self.running = False
        self.stock_list = helpers.get_stock_list_from_csv('nasdaq_screener.csv')
        self.oauth = OAuth(stockbroker_credentials)
        self.db = DatabaseManager(database_credentials=database_credentials)

    def run(self):
        self.running = True
        # TODO: Removed this for now, need to figure out why I'm retrieving this data. Currently I'm not using it, so
        #  I'm just going to comment it out for now.
        # direction_change = True
        #
        # account_watchlist = parser.get_all_stock_symbols_from_watchlist(
        #     watchlist.get_accounts_watchlists(oauth=self.oauth)
        # )
        # watchlist_counter = 1
        # time.sleep(1)  # Until a manager is implemented, this is a hack to avoid rate limiting.
        #
        # eastern = timezone(offset=timedelta(hours=-4))
        # while self.running:
        #     # TODO: Add a api call to the market hours to determine if the market is open.
        #     current_weekday = datetime.today().weekday()
        #     current_time = datetime.now(tz=eastern).time()
        #     open_time = datetime.strptime('09:30:00', '%H:%M:%S').time()
        #     close_time = datetime.strptime('16:00:00', '%H:%M:%S').time()
        #
        #     # Only run this logic on weekdays
        #     if current_weekday < 5 and open_time < current_time < close_time and False:
        #         if direction_change:
        #             equity_movers = movers.get(
        #                 oauth=self.oauth,
        #                 index=StockIndexType.NASDAQ,
        #                 direction=DirectionType.UP,
        #                 change=ValueChangeType.PERCENT
        #             )
        #         else:
        #             equity_movers = movers.get(
        #                 oauth=self.oauth, index=StockIndexType.NASDAQ,
        #                 direction=DirectionType.DOWN,
        #                 change=ValueChangeType.PERCENT
        #             )
        #         direction_change = not direction_change
        #         for mover in equity_movers:
        #             self.db.insert(
        #                 table_name='movers',
        #                 columns="change, "
        #                         "description, "
        #                         "direction, "
        #                         "last_val, "
        #                         "symbol, "
        #                         "totalVolume",
        #                 values=[mover['change'],
        #                         mover['description'],
        #                         mover['direction'],
        #                         mover['last'],
        #                         mover['symbol'],
        #                         mover['totalVolume']]
        #             )
        #     else:
        #         symbol = account_watchlist[(len(account_watchlist) - 1) % watchlist_counter]
        #         self.add_price_history_candle_to_database(
        #             symbol=symbol,
        #             period=1,
        #             period_type='day',
        #             frequency_type='minute',
        #             frequency=1)
        #         watchlist_counter += 1

        time.sleep(.7)

    def add_price_history_candle_to_database(self, symbol: str, period: int, period_type: str, frequency_type: str, frequency: int):
        price = asyncio.run(price_history.get_price_history(
            oauth=self.oauth,
            params={'period': period,
                    'periodType': period_type,
                    'frequency': frequency,
                    'frequencyType': frequency_type},
            symbol=symbol
        ))
        # Get the last candle from price history
        if not price['empty']:
            last_candle = price['candles'][len(price['candles']) - 1]
            timestamp = datetime.fromtimestamp(last_candle['datetime'] / 1000)
            self.db.insert(table_name='candles',
                           columns="close, "
                                   "high, "
                                   "low, "
                                   "open, "
                                   "symbol, "
                                   "volume, "
                                   "datetime",
                           values=[last_candle['close'],
                                   last_candle['high'],
                                   last_candle['low'],
                                   last_candle['open'],
                                   price['symbol'],
                                   last_candle['volume'],
                                   timestamp]
                           )

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, value):
        self._running = value
