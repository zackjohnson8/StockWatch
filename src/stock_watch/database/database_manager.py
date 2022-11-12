import psycopg2
import logging
from typing import Any
from .models import DatabaseCredentialModel


class Connection:
    def __init__(self, database_credentials: DatabaseCredentialModel):
        self._database_credentials = database_credentials
        self._connection = None

    def __del__(self):
        self.disconnect()

    def _connect_to_database(self) -> Any:
        try:
            self._connection = psycopg2.connect(
                f"dbname={self._database_credentials.database_name} "
                f"user={self._database_credentials.user} "
                f"host={self._database_credentials.host} "
                f"password={self._database_credentials.password}")
        except psycopg2.Error as e:
            logging.info(f"Failed to connect to database: {e}")
            raise e

    def disconnect(self):
        if self._connection is not None:
            self._connection.close()

    def get_connection(self) -> Any:
        if self._connection is None:
            self._connect_to_database()
        return self._connection


class DatabaseManager:
    def __init__(self, database_credentials: DatabaseCredentialModel):
        # Add a database connection
        self.database_connection = Connection(database_credentials=database_credentials)

    def create_table(self, table_name, columns):
        connection = self.database_connection.get_connection()
        connection.cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns + ")")
        connection.commit()

    def insert(self, table_name, columns, values: list):
        connection = self.database_connection.get_connection()
        statement = "INSERT INTO " + table_name + " (" + columns + ") VALUES (" + self._get_format_symbol(
            len(values)) + ")"
        connection.cursor.execute(statement, values)
        connection.commit()

    def _get_format_symbol(self, count):
        return_str = ""
        for i in range(count):
            return_str += "%s,"
        return return_str[:-1]
