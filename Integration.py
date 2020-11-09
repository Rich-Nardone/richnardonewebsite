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











#Landing page
@game.route('/')
def index(): 
    return flask.render_template('index.html')

#Route for the main game atm.

#@game.route("/game")
#def index():
  #  return flask.render_template("main_game.html")


@socketio.on('google login')
def google_login(data):
    # idinfo contains dictionary of user info
    userdat = data["UserInfo"]
    print("It works!")
    
    
    
# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        game,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )