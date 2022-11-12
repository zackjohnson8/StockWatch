import requests

from src.stock_watch.stockbroker.models.direction_type import DirectionType
from src.stock_watch.stockbroker.models.stock_index_type import StockIndexType
from src.stock_watch.stockbroker.models.value_change_type import ValueChangeType
from src.stock_watch.stockbroker.oauth import OAuth

import src.stock_watch.logger as logger

logging = logger.get(__name__)


def get(
        oauth: OAuth,
        index: StockIndexType,
        direction: DirectionType,
        change: ValueChangeType,
        **kwargs
) -> dict:
    response = requests.get(
        url=f'https://api.tdameritrade.com/v1/marketdata/{index.value}/movers',
        params={'direction': direction.value, 'change': change.value},
        headers={'Authorization': f'Bearer {oauth.get_token()}'},
        **kwargs
    )
    if response.status_code == 200:
        return response.json()
    else:
        return logging.error(f'Error: {response.status_code} {response.reason}')
