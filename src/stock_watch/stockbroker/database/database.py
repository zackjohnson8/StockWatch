import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            "dbname='stockdata' user='stockdata' host='localhost' password='mysecretpassword'")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table_name, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns + ")")
        self.connection.commit()

    def insert(self, table_name, columns, values):
        self.cursor.execute("INSERT INTO " + table_name + " (" + columns + ") VALUES (" + values + ")")
        self.connection.commit()

    def select(self, table_name, columns, where):
        self.cursor.execute("SELECT " + columns + " FROM " + table_name + " WHERE " + where)
        return self.cursor.fetchall()

    def select_all(self, table_name, columns):
        self.cursor.execute("SELECT " + columns + " FROM " + table_name)
        return self.cursor.fetchall()

    def update(self, table_name, column, value, where):
        self.cursor.execute("UPDATE " + table_name + " SET " + column + " = " + value + " WHERE " + where)
        self.connection.commit()

    def delete(self, table_name, where):
        self.cursor.execute("DELETE FROM " + table_name + " WHERE " + where)
        self.connection.commit()

    def delete_all(self, table_name):
        self.cursor.execute("DELETE FROM " + table_name)
        self.connection.commit()

    def drop_table(self, table_name):
        self.cursor.execute("DROP TABLE " + table_name)
        self.connection.commit()
