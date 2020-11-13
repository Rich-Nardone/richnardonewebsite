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
import models
from game import deconstructPlayer
from sqlalchemy import update
#---------------------------------


#Init of Flask
game = flask.Flask(__name__)


#SocketIO Init
socketio = flask_socketio.SocketIO(game)
socketio.init_app(game, cors_allowed_origins="*")

#database init
DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)
SQL_USER = os.environ["SQL_USER"]
SQL_PWD = os.environ["SQL_PASSWORD"]
DBUSER = os.environ["USER"]

DATABASE_URI = os.environ["DATABASE_URL"]

game.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

DB = flask_sqlalchemy.SQLAlchemy(game)
DB.init_app(game)
DB.app = game

userlist = [1]
@socketio.on('google login')
def google_login(data):
    # idinfo contains dictionary of user info
    userdat = data["UserInfo"]
    profiledat = userdat["profileObj"]
    em=profiledat["email"]
    all_email = [username.email for username in DB.session.query(models.username).all()]
    if em not in all_email:
        user = models.username(email=em)
        DB.session.add(user)
        DB.session.commit()
    userid = DB.session.query(models.username).filter_by(email=em).first()
    userlist.append(userid.id)
#Landing page
@game.route('/')
def index():
    FLAG="INSERT"
    USER = userlist[-1]
    print(USER)
    all_character = [character.characterName for character in DB.session.query(models.character).all()]
    all_userid = [user_id.user_id for user_id in DB.session.query(models.character).all()]
    dict = {}
    for i in range(len(all_character)):
        dict[all_userid[i]] = all_character[i]
    statslist = deconstructPlayer()

    for x,y in dict.items():
        if USER == x and statslist[0] == y:
            FLAG = "UPDATE"
            break
        else:
            FLAG = "INSERT"
    
    if FLAG == "INSERT":
        chara = models.character(user_id=USER,characterName=statslist[0],strength=statslist[1],dex=statslist[2],con=statslist[3],intel=statslist[4],cha=statslist[5],luck=statslist[6],max_health=statslist[7],health=statslist[8],max_mana=statslist[9],mana=statslist[10],money=statslist[11], checkpoint=statslist[12])
        DB.session.add(chara)
        DB.session.commit()
    elif FLAG == "UPDATE":
        chara = DB.session.query(models.character).filter_by(user_id=USER, characterName=statslist[0]).first()
        chara.strength = statslist[1]
        chara.dex = statslist[2]
        chara.con = statslist[3]
        chara.intel = statslist[4]
        chara.cha = statslist[5]
        chara.luck = statslist[6]
        chara.max_health = statslist[7]
        chara.health = statslist[8]
        chara.max_mana = statslist[9]
        chara.mana = statslist[10]
        chara.money = statslist[11]
        chara.checkpoint = statslist[12]
        DB.session.commit()
    else:
        print("weird error")

    
    return flask.render_template('index.html')

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