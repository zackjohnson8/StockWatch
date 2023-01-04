import psycopg2

from flask import g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            "dbname='stockdata' user='stockdata' host='localhost' password='mysecretpassword'")

    return g.db


def init_db():
    get_db()


def init_app(app):
    app.teardown_appcontext(close_db)


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()