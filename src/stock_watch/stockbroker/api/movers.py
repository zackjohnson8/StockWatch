from src.stock_watch.stockbroker.handlers.api_handler import ApiHandler
from src.stock_watch.stockbroker.models.types.direction_type import DirectionType
from src.stock_watch.stockbroker.models.types.stock_index_type import StockIndexType
from src.stock_watch.stockbroker.models.types.value_change_type import ValueChangeType


def get(
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
