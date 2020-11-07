"""
    TODO :
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
from player import Player

def progress(user, player, checkpoint):
    """ Method for saving progress """
    # TODO Implement with PSQL
    print("DEBUG: Username "+user+" with",player,"at "+checkpoint) # DEBUG

def prompt_in():
    """ Method for receiving input """
    # TODO Use socket.io listening and work with JS
    text = input()
    return text

def send_out(msg):
    """ Method for sending reply """
    # TODO Use socket.io and work with JS
    print(">"+msg)