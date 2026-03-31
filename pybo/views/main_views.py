from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'Pybo index!'

@bp.route('/hello')
def hello_world():
    return 'Hello pybo!'

@bp.route('/login')
def login():
    return 'Hello login!'