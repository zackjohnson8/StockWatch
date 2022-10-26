import multiprocessing

from src.stock_watch import flaskr
from src.stock_watch.stockbroker.app import StockBroker
from src.stock_watch.stockbroker.docker.models import docker_credential_model
from src.stock_watch.stockbroker.models import stockbroker_credential_model


class StockWatch:

    def __init__(self):
        self.db_service = None
        self.stockbroker = None

    def run(self,
            docker_credential: docker_credential_model.DockerCredentialModel,
            stockbroker_credential: stockbroker_credential_model.StockbrokerCredentialModel,
            ):
        """
        This will start the stock watch application.
        :param docker_credential: Credentials for interacting with the docker service.
        :param stockbroker_credential: Credentials for interacting with the stockbroker service.
        :return:
        """
        self.stockbroker = StockBroker(
            stockbroker_credential=stockbroker_credential,
            docker_credential=docker_credential
        )

        p = multiprocessing.Process(target=lambda: flaskr.run())
        p.start()

        p2 = multiprocessing.Process(target=lambda: self.stockbroker.run())
        p2.start()

        p.join()
        p2.join()

        # # Create a stockbroker api handler to
        # self.tdameritrade_service = api_handler.ApiHandler(api_config)
        #
        #
        # while True:
        #     #
        #     database_service = DatabaseDockerService(
        #         docker_username=args.docker_user,
        #         docker_password=args.docker_password,
        #         docker_compose_file='docker/database/docker_compose/docker-compose-database.yml',
        #         working_dir=working_dir
        #     )
        #     database_service.stop_database()
        #     database_service.start_database()
        #
        #     stockbroker.run(api_handler, StockIndexType.NASDAQ, DirectionType.UP, ValueChangeType.PERCENT)
        #
        #     database_api = DatabaseAPI()
        #     database_api.insert_movers(movers)
