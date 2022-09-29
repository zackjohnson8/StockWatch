import sys

from stock_watch_app.src.handlers.api_handler import ApiHandler
from stock_watch_app.src.handlers.arg_handler import ArgumentHandler
from stock_watch_app.src.models.api_config import APIConfig
from stock_watch_app.tdameritrade.apis import movers_api
from stock_watch_app.tdameritrade.models.types.direction_type import DirectionType
from stock_watch_app.tdameritrade.models.types.stock_index_type import StockIndexType
from stock_watch_app.tdameritrade.models.types.value_change_type import ValueChangeType


def main(argv):
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args(argv)
    api_configs = APIConfig(args.refresh, args.client, args.url, args.access)
    api_handler = ApiHandler(api_configs)

    movers = movers_api.get_movers(api_handler, StockIndexType.NASDAQ, DirectionType.UP, ValueChangeType.PERCENT)
    pass

if __name__ == '__main__':
    main(sys.argv[1:])
