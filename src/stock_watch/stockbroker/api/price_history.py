from __future__ import annotations
from typing import Any
from src.stock_watch.stockbroker.oauth import OAuth
import aiohttp as aiohttp
import logging


async def get_price_history(
        oauth: OAuth,
        symbol: str,
        params: dict = None,
        **kwargs
) -> Any | None:
    url = f'https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory'
    headers = {'Authorization': f'Bearer {oauth.get_token()}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return logging.error(f'Error: {response.status} {response.reason}')
