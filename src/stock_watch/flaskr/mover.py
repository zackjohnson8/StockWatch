from flask import (
    Blueprint, json
)

from src.stock_watch.flaskr.db import get_db

bp = Blueprint('mover', __name__, url_prefix='/mover')


@bp.route('/top')
def top():
    db = get_db()
    db_cursor = db.cursor()
    db_cursor.execute(
        'SELECT * FROM movers WHERE direction = %s',  ('up',)
    )
    rows = db_cursor.fetchall()
    db_cursor.close()
    return json.dumps(rows)


@bp.route('/bottom')
def bottom():
    db = get_db()
    db_cursor = db.cursor()
    db_cursor.execute(
        'SELECT * FROM movers WHERE direction = %s',  ('down',)
    )
    rows = db_cursor.fetchall()
    db_cursor.close()
    return json.dumps(rows)
