#---------------------------------
#Will integrate database and email
#---------------------------------
#Libraries to be used
#---------------------------------
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio

import random
import json
import requests
from flask import request
#---------------------------------


#Init of Flask
game = flask.Flask(__name__)


#SocketIO Init
socketio = flask_socketio.SocketIO(game)
socketio.init_app(game, cors_allowed_origins="*")




#Route for the main game atm.

#@game.route("/game")
#def index():
  #  return flask.render_template("main_game.html")


# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        game,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )