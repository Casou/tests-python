from flask import jsonify, Blueprint

from tests_basile import app
from tests_basile.model import People
from tests_basile.schema import peoples_schema

context_path = app.config['CONTEXT_PATH']
bp = Blueprint('people', __name__, url_prefix=f'{context_path}/')


@bp.route('/peoples', methods=['GET'])
def people_find_all():
    all = People.query.all()
    result = peoples_schema.dump(all)
    return jsonify(result.data)
