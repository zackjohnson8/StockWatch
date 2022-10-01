import sys

from src.extends import logger
from src.handlers.api_handler import ApiHandler
from src.handlers.arg_handler import ArgumentHandler
from src.models.api_config import APIConfig
from tdameritrade.apis import movers_api
from tdameritrade.models.types.direction_type import DirectionType
from tdameritrade.models.types.stock_index_type import StockIndexType
from tdameritrade.models.types.value_change_type import ValueChangeType

logging = logger.get_logger(__name__)


def main(argv):
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args(argv)
    api_configs = APIConfig(args.refresh, args.client, args.url, args.access)
    api_handler = ApiHandler(api_configs)

    movers = movers_api.get_movers(api_handler, StockIndexType.NASDAQ, DirectionType.UP, ValueChangeType.PERCENT)
    print(movers)


if __name__ == '__main__':
    logging.info('Starting main.py')
    main(sys.argv[1:])
