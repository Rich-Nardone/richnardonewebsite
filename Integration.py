#---------------------------------
#Will integrate database and email
#---------------------------------
#Libraries to be used
#---------------------------------
import os
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from dotenv import load_dotenv

#For shop, checks if item has been purchased.
item=0
#Used to check if user bought item again.
times=1

import random
import json
import requests
import models
import game.game
import game.game_io
from game.game import game, scenario
from game.game_io import progress, prompt_in, send_out, deconstructPlayer
from game.player import Player
from sqlalchemy import update

game = flask.Flask(__name__)


socketio = flask_socketio.SocketIO(game)
socketio.init_app(game, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

database_uri = os.environ["DATABASE_URL"]
game.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(game)
db.init_app(game)
db.app = game

#===================================================================================




#For shop, checks if item has been purchased.
item=0
#Used to check if user bought item again.
times=1


#function that marks and saves progress, either inserting a new character into database or updating an existing one.
def saveProgress():
    FLAG="INSERT"
    USER = userlist[-1]
    all_character = [character.characterName for character in db.session.query(models.character).all()]
    all_userid = [user_id.user_id for user_id in db.session.query(models.character).all()]
    dict = {}
    for i in range(len(all_character)):
        dict[all_userid[i]] = all_character[i]
        
    USER=userlist[-1]
    email = db.session.query(models.username).filter_by(id=USER).first()
    key = email.id
    characterList = db.session.query(models.character).filter_by(user_id=key)    
    
    player = Player()
    #needs to pick character by user choice
    for char in characterList:
        if char.characterName == "popo":
            player = char

    statslist = deconstructPlayer(player)

    for x,y in dict.items():
        if USER == x and statslist[0] == y:
            FLAG = "UPDATE"
            break
        else:
            FLAG = "INSERT"
    
    if FLAG == "INSERT":
        chara = models.character(user_id=USER,characterName=statslist[0],str=statslist[1],dex=statslist[2],con=statslist[3],int=statslist[4],cha=statslist[5],luck=statslist[6],max_health=statslist[7],health=statslist[8],max_mana=statslist[9],mana=statslist[10],money=statslist[11], checkpoint=statslist[12], gender=statslist[13],characterClass=statslist[14])
        db.session.add(chara)
        db.session.commit()
    elif FLAG == "UPDATE":
        chara = db.session.query(models.character).filter_by(user_id=USER, characterName=statslist[0]).first()
        chara.str = statslist[1]
        chara.dex = statslist[2]
        chara.con = statslist[3]
        chara.int = statslist[4]
        chara.cha = statslist[5]
        chara.luck = statslist[6]
        chara.max_health = statslist[7]
        chara.health = statslist[8]
        chara.max_mana = statslist[9]
        chara.mana = statslist[10]
        chara.money = statslist[11]
        chara.checkpoint = statslist[12]
        chara.gender = statslist[13]
        chara.characterClass = statslist[14]
        db.session.commit()
    else:
        print("weird error")

def player_info():
    #player_info = 'lol'
    player_info = {'user_party': ['player1', 'player2', 'player10'], 'user_inventory': ['coins', 'sword', 'shield'], 'user_chatlog': ['welcome to the world', 'attack', 'user attacks, hitting the blob for 10pts']}
    if item==1:
        x=player_info['user_inventory']
        global times
        if times==0:
            x.extend(["Health Pack"])
            times+=1
        else:
            x.extend(["Health Pack"]*times)
            times+=1
            
        print(x)
        player_info['user_inventory']=x
    socketio.emit('player info', player_info)

userlist = [1]
@socketio.on('google login')
def google_login(data):
    # idinfo contains dictionary of user info
    userdat = data["UserInfo"]
    profiledat = userdat["profileObj"]
    em=profiledat["email"]
    
    all_email = [username.email for username in db.session.query(models.username).all()]
    if em not in all_email:
        user = models.username(email=em)
        db.session.add(user)
        db.session.commit()
    userid = db.session.query(models.username).filter_by(email=em).first()
    userlist.append(userid.id)
    
    
@socketio.on('user input')
def parse_user_input(data):
    print(data['input']) #This is what user inputs into the chat command page. Parse data in order to interact with game logic
    
    
@socketio.on('user onchat')
def user_arrived(): 
    #THIS IS JUST TEST INPUT THAT IS RECIEVED ON THE FRONTEND SOCKET
    player_info()
    

#Test atm for the shop
@socketio.on('item purchased')
def item_purchased():
    global item
    item=1
    player_info()
    
        
    
@socketio.on('user new character')
def character_creation(data):
    print(data)
    
#======================================================================================
@game.route('/')
def index(): 
    return flask.render_template('index.html')
#======================================================================================
@game.route('/character_creation.html')
def char_create(): 
    return flask.render_template('character_creation.html')
    
#=======================================================================================   
@game.route('/main_chat.html')
def main():
   saveProgress()
   return flask.render_template('main_chat.html')
    
#=======================================================================================


# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        game,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )