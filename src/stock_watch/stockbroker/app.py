from src.stock_watch.stockbroker.database.services import database_service
from src.stock_watch.stockbroker.docker.models import docker_credential_model
from src.stock_watch.stockbroker.models import stockbroker_credential_model
from src.stock_watch.stockbroker.services import stockbroker_service


class StockBroker:
    """
    This class is used to handle the running of the stockbroker package. Call the run method to start the process.
    """
    def __init__(self, stockbroker_credential: stockbroker_credential_model.StockbrokerCredentialModel,
                 docker_credential: docker_credential_model.DockerCredentialModel):
        """
        :param stockbroker_credential: The credentials for accessing the stockbroker api.
        :param docker_credential: The credentials for accessing the docker service.
        """
        # The stockbroker needs a database to store data in from the stockbroker api calls
        self.db_service = database_service.DatabaseService(docker_credentials=docker_credential)

        # The stockbroker needs to make api calls to the stockbroker api to retrieve data
        self.api_service = stockbroker_service.StockbrokerService(stockbroker_credential=stockbroker_credential)

    def run(self):
        """
        This method is used to run the stockbroker package.
        """
        self.db_service.run()
        self.api_service.run()
