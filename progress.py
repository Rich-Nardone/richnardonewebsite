"""
    Helpful file to streamline saving and loading players' progress from the database
"""

import os
import models
from settings import db

from game.player import Player, deconstruct_player

# for this funciton work a list of users with most recent ones at the end must be sent
def save_progress(userlist):
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


# need to send list of users to use function, also this is currnetly incomplete
def load_progress(userlist, char_name):
    """
        Loads all characters from DB
        -> userlist is the list of most recent users
        -> Tries to match char_name with user from DB
        <- Returns a Player obj if found, otherwise returns None
    """
    USER = userlist[-1]
    email = db.session.query(models.username).filter_by(id=USER).first()
    key = email.id
    characterList = db.session.query(models.character).filter_by(user_id=key)
    # gets all the character names tied to userID. Need to display all names and allowed use to select or create new
    player = None
    for char in characterList:
        if char.characterName == char_name:
            player = char
    return player
