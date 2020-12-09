"""
    Launches the Flask app
"""
import os
import flask
from settings import db, app, socketio
from inventory import (
    get_user_inventory,
    get_asc_inventory,
    get_dsc_inventory,
    search_bar,
    filter_by_type,
)

from user_controller import User
import models

# game logic
from game.game import game
from game.game_io import user_in
from game.player import Player

# For shop, checks if item has been purchased.
ITEM = 0
# Used to check if user bought item again.
TIMES = 1


def player_info():
    """ Send playerinfo to js. Currently sends dummy data. """
    player_data = {
        "user_party": ["player1", "player2", "player10"],
        "user_inventory": ["coins", "sword", "shield"],
        "user_chatlog": [
            "welcome to the world",
            "attack",
            "user attacks, hitting the blob for 10pts",
        ],
    }
    if ITEM == 1:
        inv = player_data["user_inventory"]
        global TIMES
        if TIMES == 0:
            inv.extend(["Health Pack"])
            TIMES += 1
        else:
            inv.extend(["Health Pack"] * TIMES)
            TIMES += 1

        print(inv)
        player_data["user_inventory"] = inv
    socketio.emit("player info", player_data)


userlist = [1]
idlist = [""]


def create_user_controller(email):
    """ Creates a session for a user given an email """
    userObj = User(email)
    flask.session["userObj"] = userObj


@socketio.on("google login")
def google_login(data):
    """ Google Login """
    # idinfo contains dictionary of user info
    userdat = data["UserInfo"]
    profiledat = userdat["profileObj"]
    em = profiledat["email"]
    all_email = [username.email for username in db.session.query(models.username).all()]
    if em not in all_email:
        user = models.username(email=em)
        db.session.add(user)
        db.session.commit()
    userid = db.session.query(models.username).filter_by(email=em).first()
    userlist.append(userid.id)

    # Used to distinguish users, for database user calls
    create_user_controller(em)

    flask.session["user_id"] = em
    idlist.append(em)

    # check if user has character
    userObj = flask.session["userObj"]
    response = {}

    if userObj.user_exists():
        if userObj.character_counter > 0:
            response["has_character"] = True
        else:
            response["has_character"] = False
    else:
        response["has_character"] = False

    socketio.emit("google login response", response)


@socketio.on("email login")
def email_login(data):
    print(data)
    create_user_controller(data)

    userObj = flask.session["userObj"]
    response = {}

    if userObj.user_exists():
        response["user_exists"] = True
        if userObj.character_counter > 0:
            response["has_character"] = True
        else:
            response["has_character"] = False
    else:
        response["user_exists"] = False
        response["has_character"] = False

    socketio.emit("email exists", response)


def send_party():
    user_party = ["player1", "player2", "player10"]
    socketio.emit("user party", user_party)


def send_chatlog(user_chatlog):
    socketio.emit("user chatlog", user_chatlog)

charlist = [1]
@socketio.on("choosen character")
def character_selected(data):
    charlist.append(data)
    db.session.query(models.charlist).delete()
    char = models.charlist(char=data)
    db.session.add(char)
    db.session.commit()
    if "userObj" in flask.session:
        userObj = flask.session["userObj"]
        userObj.char_select(data)
        flask.session["userObj"] = userObj
        print(userObj.selected_character_id)

#character id is hard coded
@socketio.on("user input")
def parse_user_input(data):
    """ Parse user inputs in order to interact with game logic """
    message = data["input"]
    chat = models.chat_log(chat=message,character_id=charlist[-1])
    db.session.add(chat)
    db.session.commit()
    user_in.update(data["input"])


@socketio.on("get party")
def get_party():
    send_party()


@socketio.on("get inventory")
def get_inventory():
    userObj = flask.session["userObj"]
    inventory = userObj.get_inventory()
    send_inventory(inventory)


def send_inventory(inventory):
    socketio.emit("user inventory", inventory)


@socketio.on("get chatlog")
def get_chatlog():
    log = get_user_log()
    send_log(log)


# Start game
@socketio.on("game start")
def game_start():
    player = Player()
    # try to grab player object from db if possible
    userObj = flask.session["userObj"]
    for x in db.session.query(models.character).filter(models.character.id==userObj.selected_character_id):
        dat = x
        game(dat)


def get_user_log():
    return show_log()

def send_log(log):
    socketio.emit("user chatlog", log)

def show_log():
    userObj = flask.session["userObj"]
    log = userObj.retrive_chatlog()
    print(log)
    return log

# Test atm for the shop
@socketio.on("item purchased")
def item_purchased():
    """ Purchase item """
    global ITEM
    ITEM = 1
    player_info()


@socketio.on("get user characters")
def user_chars():
    print("landed")
    characters = {}
    userObj = flask.session["userObj"]
    characters["char_instance"] = userObj.get_characters()
    socketio.emit("recieve user characters", characters)


@socketio.on("user new character")
def character_creation(data):
    """ Create character """
    player = Player()
    player.id = data["name"]
    player.gen = data["gen"]
    player.character_class = data["classType"]
    # data includes character attributes: name, gender and character class
    if data["classType"] == "Jock":
        player.make_jock()
    elif data["classType"] == "Bookworm":
        player.make_bookworm()
    elif data["classType"] == "NEET":
        player.make_neet()
    USER = userlist[-1]
    email = db.session.query(models.username).filter_by(id=USER).first()
    userid = email.id
    dbplayer = models.character(
        user_id=userid,
        character_class=data["classType"],
        character_name=data["name"],
        gender=data["gen"],
        strength=player.strength,
        dex=player.dex,
        con=player.con,
        intel=player.intel,
        cha=player.cha,
        luck=player.luk,
        max_health=player.max_health,
        health=player.health,
        max_mana=player.max_mana,
        mana=player.mana,
        money=player.money,
    )
    db.session.add(dbplayer)
    db.session.commit()
    userObj = flask.session["userObj"]
    for x in models.db.session.query(models.character).filter(models.character.user_id == dbplayer.user_id, models.character.character_name == data["name"]):
        print(x.character_name)
        print(x.id)
        userObj.char_select(x.id)
        
    flask.session["userObj"] = userObj
        
        


# ======================================================================================
@app.route("/")
def about():
    """ main page """
    return flask.render_template("landing_page.html")


# =======================================================================================


@app.route("/character_selection.html")
def char_select():
    """ main page """
    return flask.render_template("character_selection.html")


# =======================================================================================


@app.route("/login.html")
def index():
    """ main page """
    return flask.render_template("index.html")


# ======================================================================================
@app.route("/character_creation.html")
def char_create():
    """ character creation page """
    return flask.render_template("character_creation.html")


# =======================================================================================
@app.route("/main_chat.html")
def main():
    """ main chat window """
    show_log()
    return flask.render_template("main_chat.html")


# =========================================================================================
@app.route("/options.html")
def options():
    """ main chat window """
    # save_progress()
    print(idlist[-1] + " YOOOOO")
    return flask.render_template("options.html")


# =======================================================================================

# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
