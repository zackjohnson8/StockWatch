from src.stock_watch import helpers
from src.stock_watch.app import StockWatch
from src.stock_watch.stockbroker.docker.models import docker_credential_model
from src.stock_watch.stockbroker.models import stockbroker_credential_model

import src.stock_watch.logger as logger

logging = logger.get(__name__)


def main():

    # Use helpers to retrieve credentials from the startup_configs
    startup_config = helpers.read_yaml_file('./src/stock_watch/configs/startup_config.yml')

    docker_credentials = docker_credential_model.DockerCredentialModel(
        username=helpers.check_value(startup_config['dockerhub']['username']),
        password=helpers.check_value(startup_config['dockerhub']['password'])
    )

    stockbroker_credentials = stockbroker_credential_model.StockbrokerCredentialModel(
        client_id=helpers.check_value(startup_config['stockbroker']['client_id']),
        redirect_url=helpers.check_value(startup_config['stockbroker']['redirect_uri']),
        refresh_token=helpers.check_value(startup_config['stockbroker']['refresh_token'])
    )

    stock_watch = StockWatch()
    stock_watch.run(
        docker_credential=docker_credentials,
        stockbroker_credential=stockbroker_credentials
    )


if __name__ == '__main__':
    logging.info('Starting main.py')
    main()
