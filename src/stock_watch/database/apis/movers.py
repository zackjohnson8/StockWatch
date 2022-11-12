import psycopg2


class Movers:
    def __init__(self):
        self.connection = psycopg2.connect(
            "dbname='stockdata' user='stockdata' host='localhost' password='mysecretpassword'")

    def insert_movers(self, movers):
        cursor = self.connection.cursor()
        for mover in movers:
            cursor.execute(
                "INSERT INTO movers (change, description, direction, last_val, symbol, totalVolume) "
                "VALUES (%s, %s, %s, %s, %s, %s);",
                (mover['change'], mover['description'], mover['direction'], mover['last'], mover['symbol'],
                 mover['totalVolume']))
        self.connection.commit()
        cursor.close()

    def fetch_movers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM movers;")
        movers = cursor.fetchall()
        cursor.close()
        return movers
