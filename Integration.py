"""
    Launches the Flask app
"""
import os
from os.path import join, dirname
from settings import db, app, socketio
import models
import flask
# tests

# game logic
import game.game
import game.game_io
from game.game import game
from game.game_io import deconstruct_player
from game.player import Player

# For shop, checks if item has been purchased.
item = 0
# Used to check if user bought item again.
times = 1

def saveProgress():
    """ Saves the user's progress to the database """
    FLAG = "INSERT"
    USER = userlist[-1]
    all_character = [
        character.character_name
        for character in db.session.query(models.character).all()
    ]
    all_userid = [
        user_id.user_id for user_id in db.session.query(models.character).all()
    ]
    dict = {}
    for i in range(len(all_character)):
        dict[all_userid[i]] = all_character[i]

    USER = userlist[-1]
    email = db.session.query(models.username).filter_by(id=USER).first()
    key = email.id
    characterList = db.session.query(models.character).filter_by(user_id=key)

    player = Player()
    # needs to pick character by user choice
    for char in characterList:
        if char.character_name == "popo":
            player = char

    statslist = deconstruct_player(player)

    for x, y in dict.items():
        if USER == x and statslist[0] == y:
            FLAG = "UPDATE"
            break
        else:
            FLAG = "INSERT"

    if FLAG == "INSERT":
        chara = models.character(
            user_id=USER,
            character_name=statslist[0],
            strength=statslist[1],
            dex=statslist[2],
            con=statslist[3],
            intel=statslist[4],
            cha=statslist[5],
            luck=statslist[6],
            max_health=statslist[7],
            health=statslist[8],
            max_mana=statslist[9],
            mana=statslist[10],
            money=statslist[11],
            checkpoint=statslist[12],
            gender=statslist[13],
            character_class=statslist[14],
        )
        db.session.add(chara)
        db.session.commit()
    elif FLAG == "UPDATE":
        chara = (
            db.session.query(models.character)
            .filter_by(user_id=USER, character_name=statslist[0])
            .first()
        )
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
        chara.gender = statslist[13]
        chara.character_class = statslist[14]
        db.session.commit()
    else:
        print("weird error")


def player_info():
    """ Send playerinfo to js. Currently sends dummy data. """
    player_info = {
        "user_party": ["player1", "player2", "player10"],
        "user_inventory": ["coins", "sword", "shield"],
        "user_chatlog": [
            "welcome to the world",
            "attack",
            "user attacks, hitting the blob for 10pts",
        ],
    }
    if item == 1:
        x = player_info["user_inventory"]
        global times
        if times == 0:
            x.extend(["Health Pack"])
            times += 1
        else:
            x.extend(["Health Pack"] * times)
            times += 1

        print(x)
        player_info["user_inventory"] = x
    socketio.emit("player info", player_info)

def show_inventory():
        #need to get character id from character selection page for load game 
        dump = db.session.query(models.inventory).filter_by(character_id="1")
        inventory = []
        for item in dump:
            inventory.append(item.items)
        return inventory

def item_sort_asc():
    inventory = []
    #empties the "sorted" item table
    db.session.query(models.inventory_asc).delete()
    db.session.commit()
    #creates a dump of sorted values from the inventory table
    unsorted = db.session.query(models.inventory).order_by(models.inventory.items.asc())
    #loops through the dump and grabs all the items for the current character, adds them to the sorted items table
    for value in unsorted:
        sorted_item = models.inventory_asc(items=value.items, character_id= value.character_id)
        db.session.add(sorted_item)
        db.session.commit()
    """
    this key value is hard coded for now
    """
    key = 1
    personal_items = db.session.query(models.inventory_asc).filter_by(character_id=key)
    #currently this is just to print the sorted table as a test to make sure it works, in the future it should connect with front end to visually display the items sorted, probably best to send a list?
    for item in personal_items:
        inventory.append(item.item)
    return inventory

def item_sort_dsc():
    #empties the "sorted" item table
    db.session.query(models.inventory_dsc).delete()
    db.session.commit()
    #creates a dump of sorted values from the inventory table
    unsorted = db.session.query(models.inventory).order_by(models.inventory.items.desc())
    #loops through the dump and grabs all the items for the current character, adds them to the sorted items table
    for value in unsorted:
        sorted_item = models.inventory_dsc(items=value.items, character_id=value.character_id)
        db.session.add(sorted_item)
        db.session.commit()
    """
    this key value is hard coded for now
    """
    key = 1
    personal_items = db.session.query(models.inventory_dsc).filter_by(character_id=key)
    #currently this is just to print the sorted table as a test to make sure it works, in the future it should connect with front end to visually display the items sorted, probably best to send a list?
    for item in personal_items:
        print(item.items)

def filter_by_type():
    """
    itemType is hard coded for now, should actually be fetched from front end. key is also hard coded, same as it is for item sort asc/dsc
    """
    itemType = "weapon"
    key = 1
    filtered_items = db.session.query(models.inventory).filter_by(item_type=itemType, character_id=key)
    
    for item in filtered_items:
        print(item.items)

def search_bar():
    items = db.session.query(models.inventory)
    search = "a"
    #this is a substring search function for the inventory, right now a is hardcoded but what should be done is fetching a search field and inserting it in as a variable
    for item in items:
        if search in item.items:
            print(item.items)


userlist = [1]

idlist = [""]
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

    #Used to distinguish users, for database user calls 
    flask.session["user_id"] = em
    idlist.append(em)
    #check if user has character
def send_party(): 
    #TODO get party from database 
    
    #DUMMY DATA
    user_party=["player1", "player2", "player10"]
    socketio.emit('user party', user_party)


def get_user_inventory():
    return show_inventory()
    
    
def send_chatlog():
    #TODO get chatlog from database
    
    #DUMMY DATA
    user_chatlog=[
            "welcome to the world",
            "attack",
            "user attacks, hitting the blob for 10pts"
    ]
    socketio.emit('user chatlog', user_chatlog)

def get_asc_inventory(): 
    return item_sort_asc()

@socketio.on("user input")
def parse_user_input(data):
    """ Parse user inputs in order to interact with game logic """
    print(
        data["input"]
    )


@socketio.on("get party")
def get_party():
    send_party()
    
@socketio.on("get inventory")
def get_inventory():
    inventory = get_user_inventory()
    send_inventory(inventory)

def send_inventory(inventory):
    socketio.emit('user inventory', inventory)

@socketio.on("get chatlog")
def get_chatlog():
    #TODO get chatlog from database
    
    #DUMMY DATA
    user_chatlog=[
            "welcome to the world",
            "attack",
            "user attacks, hitting the blob for 10pts"
    ]
    send_chatlog()

# Test atm for the shop
@socketio.on("item purchased")
def item_purchased():
    """ Purchase item """
    global item
    item = 1
    player_info()


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


# ======================================================================================
@app.route("/")
def about():
    """ main page """
    return flask.render_template("landing_page.html")

#=======================================================================================
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
    saveProgress()
    return flask.render_template("main_chat.html")
    

#=========================================================================================
@app.route("/options.html")
def options():
    """ main chat window """
    #saveProgress()
    print(idlist[-1] + " YOOOOO")
    return flask.render_template("options.html")


# =======================================================================================

# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True
    )
