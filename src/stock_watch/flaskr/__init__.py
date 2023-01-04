import os
from flask import Flask

host = '0.0.0.0'
port = 5678
app = None

def create_app(test_config=None):
    global app
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    from . import index
    app.register_blueprint(index.bp)

def run():
    global app
    if not app:
        create_app()
    custom_port = int(os.environ.get('PORT', 5678))
    app.run(host='0.0.0.0', port=custom_port, debug=True)
