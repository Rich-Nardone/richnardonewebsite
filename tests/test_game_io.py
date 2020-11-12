"""
    This file tests all methods in game_io.py
    TODO:
    - unit tests with mocked socket.io and mocked PSQL
"""
import unittest
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe)))
parentdir=  os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from game import game_io

class GameIOTestCase(unittest.TestCase):
    # not even writing the test for it rn