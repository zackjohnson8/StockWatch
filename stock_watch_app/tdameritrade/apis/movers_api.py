from stock_watch_app.src.handlers.api_handler import ApiHandler
from stock_watch_app.tdameritrade.models.types.direction_type import DirectionType
from stock_watch_app.tdameritrade.models.types.stock_index_type import StockIndexType
from stock_watch_app.tdameritrade.models.types.value_change_type import ValueChangeType


def get_movers(
        api_handler: ApiHandler,
        index: StockIndexType,
        direction: DirectionType,
        change: ValueChangeType
) -> dict:
    response = api_handler.get(
        url=f'https://api.tdameritrade.com/v1/marketdata/{index.value}/movers',
        params={'direction': direction.value, 'change': change.value}
    )
    return response
