"""
    This file tests all methods in game.py and player.py
"""
import unittest
import os, sys, inspect
from unittest import MagicMock, MockResponse

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe)))
parentdir=  os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from game import game, scenario
from game import Player

test_unset_player = Player()

class GameTestCase(unittest.TestCase):
    def test_game(self):
        # Mock scenario
        game.scenario = MagicMock(
            return_value=MockResponse(
                {test_unset_player, 'end'}
            )
        )
        self.assertEqual(game('test'), 'test')

class PlayerTestCase(unittest.TestCase):
    def test_player_death(self):
        self.assertFalse(test_unset_player.is_dead())
        self.assertTrue(test_unset_player.damage(1500))

    def test_player_object(self):
        self.assertEqual(test_unset_player.str, 0)
        self.assertEqual(test_unset_player.dex, 0)
        self.assertEqual(test_unset_player.con, 0)
        self.assertEqual(test_unset_player.int, 0)
        self.assertEqual(test_unset_player.cha, 0)
        self.assertEqual(test_unset_player.luk, 0)
        self.assertEqual(test_unset_player.max_health, 100)
        self.assertEqual(test_unset_player.health, 100)
        self.assertEqual(test_unset_player.max_mana, 0)
        self.assertEqual(test_unset_player.mana, 0)
        self.assertEqual(test_unset_player.money, 0)

if __name__ == "__main__":
    unittest.main()