import os
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from flask_session import Session
from flask_session import SqlAlchemySessionInterface
from dotenv import load_dotenv

# Holds db and app variables

app = flask.Flask(__name__)


socketio = flask_socketio.SocketIO(app, manage_session=False)
socketio.init_app(app, cors_allowed_origins="*")

