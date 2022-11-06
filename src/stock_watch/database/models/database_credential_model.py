class DatabaseCredentialModel:
    def __init__(self, database_name, user, host, password):
        self.database_name = database_name
        self.user = user
        self.host = host
        self.password = password
