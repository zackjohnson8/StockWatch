from flask import Blueprint

# Create a bp for index
bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello World'