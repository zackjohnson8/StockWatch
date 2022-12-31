from __future__ import annotations
from typing import Any
from src.stock_watch.stockbroker.oauth import OAuth
import requests
import logging


def get_accounts_watchlists(
        oauth: OAuth,
        params: dict = None,
        **kwargs
) -> Any | None:
    response = requests.get(
        url=f'https://api.tdameritrade.com/v1/accounts/watchlists',
        params=params,
        headers={'Authorization': f'Bearer {oauth.get_token()}'},
        **kwargs
    )
    if response.status_code == 200:
        return response.json()
    else:
        return logging.error(f'Error: {response.status_code} {response.reason}')
