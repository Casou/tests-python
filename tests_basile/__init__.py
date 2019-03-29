from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from tests_basile.database import check_database, get_database_url

app = Flask(__name__)
app.config.from_pyfile('config.py')
# app.config.from_envvar('RADICCHIO_CONFIG', silent=True)
# app.config['APPLICATION_ROOT'] = '/radicchio'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url(app)
db = SQLAlchemy(app)

import tests_basile.model
from tests_basile.init import init_default_data

check_database(app, db)
init_default_data(db)

from tests_basile.blueprints import parameter, token, people

app.register_blueprint(parameter.bp)
app.register_blueprint(token.bp)
app.register_blueprint(people.bp)

from tests_basile.websocket import websocket_engine
