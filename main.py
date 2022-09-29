import sys

from handlers.api_handler import ApiHandler
from handlers.arg_handler import ArgumentHandler
from configs.api_config import APIConfig
from tdameritrade.apis import movers_api
from tdameritrade.models.types.direction_type import DirectionType
from tdameritrade.models.types.stock_index_type import StockIndexType
from tdameritrade.models.types.value_change_type import ValueChangeType


def main(argv):
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args(argv)
    api_configs = APIConfig(args.refresh, args.client, args.url, args.access)
    api_handler = ApiHandler(api_configs)

    movers = movers_api.get_movers(api_handler, StockIndexType.NASDAQ, DirectionType.UP, ValueChangeType.PERCENT)


if __name__ == '__main__':
    main(sys.argv[1:])
