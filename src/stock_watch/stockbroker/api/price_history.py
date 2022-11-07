import requests
from src.stock_watch.stockbroker.oauth import OAuth

import src.stock_watch.logger as logger
logging = logger.get(__name__)

def get_price_history(
        oauth: OAuth,
        symbol: str,
        params: dict = None,
        **kwargs
) -> dict:
    response = requests.get(
        url=f'https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory',
        params=params,
        headers={'Authorization': f'Bearer {oauth.get_token()}'},
        **kwargs
    )
    if response.status_code == 200:
        return response.json()
    else:
        return logging.error(f'Error: {response.status_code} {response.reason}')