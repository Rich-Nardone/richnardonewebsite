"""
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
from .player import Player
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from ..integration import save_progress

def g_save_progress(user, player):
    """ calls save_progress from integration """
    # iunno if its feasible to move the function from integration to game_io
    save_progress(player)

def load_progress(user):
    """ Method for saving progress """
    # TODO Implement with PSQL
    player = Player()
    checkpoint = ""
    return (user, player, checkpoint)  # DEBUG


def prompt_in():
    """ Method for receiving input """
    text = user_in.read_input()
    while not text:
        text = user_in.read_input()
    return text


def send_out(msg):
    """ Method for sending reply """
    socketio.emit("text", {"text": msg})


def deconstruct_player(player):
    """ Deconstructing player object for PSQL """
    # Simon wants to move this to the player.py file and player class
    statslist = [
        player.id,
        player.strength,
        player.dex,
        player.con,
        player.intel,
        player.cha,
        player.luk,
        player.max_health,
        player.health,
        player.max_mana,
        player.mana,
        player.money,
        player.checkpoint,
        player.gen,
        player.character_class,
    ]
    return statslist
