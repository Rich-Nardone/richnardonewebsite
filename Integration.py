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

db.create_all()
db.session.commit()

import models
#===================================================================================


#THESE FUNCTION SEND DUMMY DATA AT THE MOMENT. WILL UPDATE WITH DATABSE INFO EVENTUALLY
def player_info():
    #player_info = 'lol'
    player_info = {'user_party': ['player1', 'player2', 'player10'], 'user_inventory': ['coins', 'sword', 'shield'], 'user_chatlog': ['welcome to the world', 'attack', 'user attacks, hitting the blob for 10pts']}
    socketio.emit('player info', player_info)


@socketio.on('google login')
def google_login(data):
    # idinfo contains dictionary of user info
    userdat = data["UserInfo"]
    profiledat = userdat["profileObj"]
    em=profiledat["email"]
    user1 = models.username(email=em)
    db.session.add(user1)
    db.session.commit()


@socketio.on('user input')
def parse_user_input(data):
    print(data['input']) #This is what user inputs into the chat command page. Parse data in order to interact with game logic
    
    
@socketio.on('user onchat')
def user_arrived(): 
    #THIS IS JUST TEST INPUT THAT IS RECIEVED ON THE FRONTEND SOCKET
    player_info()
    
@socketio.on('user new character')
def character_creation(data):
    # data includes character attributes: name, gender and character class
    userid = '' #TODO users unique id
    dbplayer = models.character(user_id=userid,
        characterClass=data['classType'],
        characterName=data['name'],
        gender=data['gen'],
        strength=0,
        dex=0,
        con=0,
        intel=0,
        cha=0,
        luck=0,
        max_health=0,
        health=0,
        max_mana=0,
        mana=0,
        money=0)
    db.session.add(dbplayer)
    db.session.commit()
    
#======================================================================================
@game.route('/')
def index(): 
    return flask.render_template('index.html')
    
#=======================================================================================   
@game.route('/main_chat.html')
def main():
   return flask.render_template('main_chat.html')
    
#=======================================================================================
@game.route('/create')
def char_create(): 
    return flask.render_template('character_creation.html')

# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        game,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
