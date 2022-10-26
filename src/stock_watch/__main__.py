import sys

from src.stock_watch.app import StockWatch
from src.stock_watch.arguments import ArgumentParser


import src.stock_watch.logger as logger

from src.stock_watch.stockbroker.docker.models import docker_credential_model

from src.stock_watch.stockbroker.models import stockbroker_credential_model

logging = logger.get(__name__)


def main(argv):
    arg_handler = ArgumentParser()
    args = arg_handler.parse_args(argv)

    docker_credentials = docker_credential_model.DockerCredentialModel(
        username=args.docker_user,
        password=args.docker_password
    )

    stockbroker_credentials = stockbroker_credential_model.StockbrokerCredentialModel(
        refresh_token=args.access,
        client_id=args.client,
        redirect_url=args.url,
        access_token=args.refresh
    )

    stock_watch = StockWatch()
    stock_watch.run(
        docker_credential=docker_credentials,
        stockbroker_credential=stockbroker_credentials
    )


if __name__ == '__main__':
    logging.info('Starting main.py')
    main(sys.argv[1:])
