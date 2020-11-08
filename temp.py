import os
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from dotenv import load_dotenv

APP = flask.Flask(__name__)

SOCKETIO = flask_socketio.SocketIO(APP)
SOCKETIO.init_app(APP, cors_allowed_origins="*")

DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)
SQL_USER = os.environ["SQL_USER"]
SQL_PWD = os.environ["SQL_PASSWORD"]
DBUSER = os.environ["USER"]

DATABASE_URI = os.environ["DATABASE_URL"]

APP.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

DB = flask_sqlalchemy.SQLAlchemy(APP)
DB.init_app(APP)
DB.app = APP

import models

@APP.route("/")
def index():
    user1 = models.username(email="matthewcarnevale1@gmail.com")
    DB.session.add(user1)
    DB.session.commit()
    user2 = models.username(email="martycarnevale1@gmail.com")
    DB.session.add(user2)
    DB.session.commit()
    marty = models.character(characterName="marty", userid=user1)
    DB.session.add(marty)
    DB.session.commit()
    johnny = models.character(characterName="johnny",userid=user1)
    DB.session.add(johnny)
    DB.session.commit()
    toilet = models.character(characterName="toilet",userid=user2)
    DB.session.add(toilet)
    DB.session.commit()
    item1 = models.inventory(items="big stick", characterid=marty)
    DB.session.add(item1)
    DB.session.commit()
    return flask.render_template("index.html")    



if __name__ == "__main__":
    SOCKETIO.run(
        APP,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )