import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from src.stock_watch.flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.args.get('username')
        password = request.args.get('password')
        db = get_db()
        db_cursor = db.cursor()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        db_cursor.execute(
            'SELECT id FROM accounts WHERE username = %s', (username,)
        )
        if db_cursor.fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db_cursor.execute(
                'INSERT INTO accounts (username, password) VALUES (%s, %s)',
                (username, generate_password_hash(password))
            )
            db.commit()
            db_cursor.close()
            return json.dumps({'success': True, 'code': 200, 'ContentType': 'application/json'})
        return json.dumps({'success': False, 'message': error, 'ContentType': 'application/json'})


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/tester')
def test():
    return 'Test123'


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
