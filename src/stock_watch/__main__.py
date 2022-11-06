from src.stock_watch import helpers
from src.stock_watch.app import StockWatch
from src.stock_watch.docker.models.docker_credential_model import DockerCredentialModel
from src.stock_watch.database.models.database_credential_model import DatabaseCredentialModel

import src.stock_watch.logger as logger
from src.stock_watch.stockbroker.models.stockbroker_credential_model import StockbrokerCredentialModel

logging = logger.get(__name__)


def main():
    stock_watch = StockWatch()
    stock_watch.run()


if __name__ == '__main__':
    logging.info('Starting main.py')
    main()
