from flask_socketio import SocketIO

from tests_basile import app

socketio = SocketIO(app)


def run_websocket():
    socketio.run(app)


run_websocket()
