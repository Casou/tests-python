from flask import jsonify, Blueprint
from tests_basile import app
from tests_basile.model import Token
from tests_basile.schema import tokens_schema

context_path = app.config['CONTEXT_PATH']
bp = Blueprint('token', __name__, url_prefix=f'{context_path}/token')


@bp.route('/', methods=['GET'])
def token_find_all():
    all = Token.query.all()
    result = tokens_schema.dump(all)
    return jsonify(result.data)
