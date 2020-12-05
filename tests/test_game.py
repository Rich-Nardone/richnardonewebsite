"""
    This file tests all methods in game.py and player.py
"""
import unittest
import os, sys, inspect
from unittest import MagicMock, MockResponse

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe)))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# stuff required for testing
import random
from game import game, player, scenario

test_unset_player = player.Player()
test_strong_player = player.Player("stronk", 20, 20, 20, 20, 20, 0)


class GameTestCase(unittest.TestCase):
    def test_game(self):
        # Mock scenario
        game.scenario = MagicMock(return_value=MockResponse({test_unset_player, "end"}))
        self.assertEqual(game("test"), "test")


class PlayerTestCase(unittest.TestCase):
    def test_player_attack(self):
        player.damage = MagicMock()
        # without crit
        random.randrange = MagicMock(return_value=MockResponse(100))
        test_strong_player.attack("melee", test_unset_player)
        player.damage.assert_called_once_with(20, test_strong_player)
        test_strong_player.attack("range", test_unset_player)
        player.damage.assert_called_once_with(20, test_strong_player)
        test_strong_player.attack("magic", test_unset_player)
        player.damage.assert_called_once_with(20, test_strong_player)
        # with crit
        random.randrange = MagicMock(return_value=MockResponse(1))
        test_strong_player.attack("melee", test_unset_player)
        player.damage.assert_called_once_with(40, test_strong_player)
        test_strong_player.attack("range", test_unset_player)
        player.damage.assert_called_once_with(40, test_strong_player)
        test_strong_player.attack("magic", test_unset_player)
        player.damage.assert_called_once_with(40, test_strong_player)

    def test_player_damage(self):
        # no source, no death
        (msg, form) = test_unset_player.damage(1)
        self.assertIn("1", msg)
        self.assertEqual("damage", form)
        # has source, no death
        (msg, form) = test_unset_player.damage(1, test_strong_player)
        self.assertIn("1", msg)
        self.assertIn(test_strong_player.id, msg)
        self.assertEqual("damage", form)
        # no source, death
        (msg, form) = test_unset_player.damage(1000)
        self.assertIn("1000", msg)
        self.assertEqual("death", form)
        # has source, death
        (msg, form) = test_unset_player.damage(1000, test_strong_player)
        self.assertIn("1000", msg)
        self.assertIn(test_strong_player.id, msg)
        self.assertEqual("death", form)

    def test_player_death(self):
        self.assertFalse(test_unset_player.is_dead())
        test_unset_player.damage(9999999)
        self.assertTrue(test_unset_player.is_dead())

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


class ScenarioTestCase(unittest.TestCase):
    def test_start(self):
        # TODO
        self.assertTrue(True)

    def test_scenario(self):
        # TODO
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()