import os
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from flask_session import Session
from flask_session import SqlAlchemySessionInterface
from dotenv import load_dotenv

#Holds db and app variables 

app = flask.Flask(__name__)
app.config['SESSION_TYPE'] = 'sqlalchemy'
sess = Session(app)


socketio = flask_socketio.SocketIO(app, manage_session=False)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
sess.app.session_interface.db.create_all()