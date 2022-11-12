import aiohttp as aiohttp
import requests
from src.stock_watch.stockbroker.oauth import OAuth

import src.stock_watch.logger as logger

logging = logger.get(__name__)


async def get_price_history(
        oauth: OAuth,
        symbol: str,
        params: dict = None,
        **kwargs
) -> dict:
    url = f'https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory'
    headers = {'Authorization': f'Bearer {oauth.get_token()}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return logging.error(f'Error: {response.status} {response.reason}')
