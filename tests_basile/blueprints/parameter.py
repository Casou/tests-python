from flask import jsonify, Blueprint
from tests_basile import app
from tests_basile.model import Parameter
from tests_basile.schema import parameters_schema

context_path = app.config['CONTEXT_PATH']
bp = Blueprint('parameters', __name__, url_prefix=f'{context_path}/parameter')


@bp.route('/', methods=['GET'])
def parameter_find_all():
    all = Parameter.query.all()
    result = parameters_schema.dump(all)
    return jsonify(result.data)
