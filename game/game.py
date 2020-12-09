"""
    Handles the game logic
"""

import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from progress import save_progress, load_progress

# local imports
from .scenario import scenario, start_scenario


def game(player, is_new, flask_dict):
    """ Runs the game, given a user """
    # this tuple is shaped: "Player, String" where string is the area
    state_tuple = scenario(player, "intro")
    # try to load progress, otherwise start scenario
    if is_new:
        start_scenario(player)
    else:
        state_tuple = (player, player.checkpoint, flask_dict)
    # running game
    while state_tuple[1] != "end":
        save_progress([state_tuple[0]])
        state_tuple = scenario(state_tuple[0], state_tuple[1], flask_dict)
    print("game has reached endstate")
