"""
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
from .player import Player

def progress(user, player, checkpoint):
    """ Method for saving progress """
    # TODO Implement with PSQL
    print("DEBUG: Username "+user+" with", player.id, "at "+ player.checkpoint) # DEBUG

def load_progress(user):
    """ Method for saving progress """
    # TODO Implement with PSQL
    player = Player()
    checkpoint = ''
    return (user, player, checkpoint) # DEBUG

def prompt_in():
    """ Method for receiving input """
    # Changes in combat-and-death branch
    text = input()
    return text

def send_out(msg):
    """ Method for sending reply """
    # Changes in combat-and-death branch
    print(">"+msg)

def deconstruct_player(player):
    """ Deconstructing player object for PSQL """
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
