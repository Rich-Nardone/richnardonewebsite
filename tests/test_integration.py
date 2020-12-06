"""
    This file tests all methods within the main directory
    integration.py, models.py, settings.py, user_input.py
"""

import unittest
from unittest import mock
from unittest.mock import MagicMock
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe)))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# things to be mocked
from settings import db, app, socketio
import Integration
import models, user_input

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.flask_routes = []
        self.socket_params = []

    def test_flask(self):
        # "/" : about
        # "/login.html" : index
        # "/character_creation.html" : char_create
        # "/main_chat.html" : main
        # "/options.html" : options
        for route in self.flask_routes:
            # mock and then test
            self.assertTrue(True)

    def test_db(self):
        # save_progress(player object)
        # get_user_inventory
        self.assertTrue(True)
    
    def test_rcv_sockets(self):
        # "google login" : google_login
        # "user input" : parse_user_input
        # "get party" : get_party
        # "get inventory" : get_inventory
        # "get chatlog" : get_chatlog
        # "item purchased" : item_purchased
        # "user new character" : character_creation
        for sockets in self.socket_params:
            # mock and then test TODO
            self.assertTrue(True)

    def test_send_sockets(self):
        # player_info
        # send_party
        # send chatlog
        self.assertTrue(True)