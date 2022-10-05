import os
import sys

from src.stock_watch_app.utils import logger
from src.tdameritrade.handlers.api_handler import ApiHandler
from src.stock_watch_app.handlers.arg_handler import ArgumentHandler
from src.tdameritrade.models.api_config import APIConfig
from src.database.services.database_service import DatabaseService
from src.tdameritrade.apis import movers_api
from src.tdameritrade.models.types.direction_type import DirectionType
from src.tdameritrade.models.types.stock_index_type import StockIndexType
from src.tdameritrade.models.types.value_change_type import ValueChangeType

logging = logger.get_logger(__name__)

working_dir = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args(argv)
    api_configs = APIConfig(args.refresh, args.client, args.url, args.access)
    api_handler = ApiHandler(api_configs)

    movers = movers_api.get_movers(api_handler, StockIndexType.NASDAQ, DirectionType.UP, ValueChangeType.PERCENT)

    database_service = DatabaseService(
        docker_username=args.docker_user,
        docker_password=args.docker_password,
        docker_compose_file='docker/database/docker_compose/docker-compose-database.yml',
        working_dir=working_dir
    )
    database_service.stop_database()
    database_service.start_database()


if __name__ == '__main__':
    logging.info('Starting main.py')
    main(sys.argv[1:])
