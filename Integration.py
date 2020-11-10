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
from google.oauth2 import id_token
from google.auth.transport import requests
#---------------------------------
import Player

#Init of Flask
game = flask.Flask(__name__)

#SocketIO Init
socketio = flask_socketio.SocketIO(game)
socketio.init_app(game, cors_allowed_origins="*")


#Landing page
@game.route('/')
def index(): 
    return flask.render_template('index.html')

#Route for the main game atm.

#@game.route("/game")
#def index():
  #  return flask.render_template("main_game.html")

@socketio.on('create character')
def create_character(data):
    player = Player()
    # data includes character attributes: name, gender and stats
    player.id = data['name']
    player.gen = data['gen']
    # Strength:
    player.str = int(data['str'])
    # Dexterity:
    player.dex = int(data['dex'])
    # Constitution:
    player.con = int(data['con'])
    # Intelligence:
    player.int = int(data['int'])
    # Charisma:
    player.cha = int(data['cha'])
    # Luck:
    player.luk = int(data['luk'])
    

@socketio.on('google login')
def google_login(data):
    # idinfo contains dictionary of user info
    idinfo = id_token.verify_oauth2_token(
        data['tokenId'],
        requests.Request(),
        "656111270790-6jsfgnirr63rvkth2ro0u35l4alkugrg.apps.googleusercontent.com",
    )
    
    #print(idinfo) pull data from idinfo into database
    
# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        game,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )