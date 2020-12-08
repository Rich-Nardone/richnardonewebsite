"""
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from progress import save_progress
from settings import socketio
import user_input

from .player import Player

user_in = user_input.UserInput()


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
