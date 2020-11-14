"""
    TODO :
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
from .player import Player

def progress(user, player, checkpoint):
    """ Method for saving progress """
    # TODO Implement with PSQL
    print("DEBUG: Username "+user+" with",player.id,"at "+ player.checkpoint) # DEBUG

def load_progress(user):
    """ Method for saving progress """
    # TODO Implement with PSQL
    player = Player()
    checkpoint = ''
    return (user,player,checkpoint) # DEBUG

def prompt_in():
    """ Method for receiving input """
    # TODO Use socket.io listening and work with JS
    text = input()
    return text

def send_out(msg):
    """ Method for sending reply """
    # TODO Use socket.io and work with JS
    print(">"+msg)
    
def deconstructPlayer(player):
    name = player.id
    strength = player.str
    dex = player.dex
    con = player.con
    int = player.int
    cha = player.cha
    luck = player.luk
    max_health = player.max_health
    health = player.health
    max_mana = player.max_mana
    mana = player.mana
    money = player.money
    checkpoint = player.checkpoint
    gender = player.gen
    characterClass = player.characterClass
    statslist = [name,strength,dex,con,int,cha,luck,max_health,health,max_mana,mana,money,checkpoint,gender,characterClass]
    return statslist
