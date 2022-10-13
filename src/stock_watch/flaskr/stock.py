from flask import (
    Blueprint
)

bp = Blueprint('stock', __name__, url_prefix='/stock')


@bp.route('/price_history')
def price_history(symbol):
    return "Under construction"
    # db = get_db()
    # db_cursor = db.cursor()
    # db_cursor.execute(
    #     'SELECT * FROM stock WHERE symbol = %s', (symbol,)
    # )
    # rows = db_cursor.fetchall()
    # db_cursor.close()
    # return json.dumps(rows)
