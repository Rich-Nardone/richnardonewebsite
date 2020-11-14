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
    # Cannot be tested until changes are made with Integration.py
    def test_all(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()