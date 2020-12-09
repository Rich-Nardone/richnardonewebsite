"""
    Handles the game logic
"""

import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from progress import save_progress

# local imports
from .scenario import scenario


def game(player):
    """ Runs the game, given a user """
    # try to load progress, otherwise start scenario
    state_tuple = (player, player.checkpoint)
    # running game
    # while state_tuple[1] != "end":
    #     save_progress([state_tuple[0]])
    #     state_tuple = scenario(state_tuple[0], state_tuple[1])
    print("game has reached endstate")
    