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

# things to be tested
import settings
import Integration
import models, user_input

# things to be mocked
import flask
from flask_socketio import SocketIO

ROUTE_NAME = "name"  # name of the route ie "@app.route('name')"
ROUTE_DESC = "desc.html"  # page the route goes to ie "desc.html"


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = settings.app.test_client()
        self.flask_routes = [
            {ROUTE_NAME: "/", ROUTE_DESC: "landing_page.html"},
            {ROUTE_NAME: "/login.html", ROUTE_DESC: "index.html"},
            {
                ROUTE_NAME: "/character_creation.html",
                ROUTE_DESC: "character_creation.html",
            },
            {ROUTE_NAME: "/main_chat.html", ROUTE_DESC: "main_chat.html"},
            {ROUTE_NAME: "/options.html", ROUTE_DESC: "options.html"},
        ]

    def test_flask(self):
        # ensure the route goes to the correct page
        for route in self.flask_routes:
            flask.render_template = MagicMock()
            self.app.get(route[ROUTE_NAME])
            flask.render_template.assert_called_with(route[ROUTE_DESC])


class DatabaseTestCase(unittest.TestCase):
    # list of stuff to test here:
    #  character_creation
    #  save_progress(player object)
    #  google login
    #  get_inventory -> get_user_inventory
    def setUp(self):
        self.db_params = []

    #  get_chatlog
    def test_get_chatlog(self):
        Integration.send_chatlog = MagicMock()
        Integration.get_chatlog()
        Integration.send_chatlog.assert_called_once()

    #  get_party
    def test_get_party(self):
        Integration.send_party = MagicMock()
        Integration.get_party()
        Integration.send_party.assert_called_once()

    #  item_purchased
    def test_item_purchased(self):
        Integration.player_info = MagicMock()
        Integration.item_purchased()
        Integration.player_info.assert_called_once()


class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.socket_params = []

    def test_rcv_sockets(self):
        # "user input" : parse_user_input
        # "get party" : get_party
        # "get inventory" : get_inventory
        # "get chatlog" : get_chatlog
        # "item purchased" : item_purchased
        # "user new character" : character_creation
        for sockets in self.socket_params:
            # mock and then test TODO
            self.assertTrue(True)


class SocketTestCase(unittest.TestCase):
    """ testing socketio emissions """

    def setUp(self):
        self.socket_params = []

    def test_player_info(self):
        SocketIO.emit = MagicMock()
        Integration.player_info()
        SocketIO.emit.assert_called()
        # cannot do assert_called_with since playerinfo might be inconsistent in the future
    
    def test_send_chatlog(self):
        SocketIO.emit = MagicMock()
        Integration.send_chatlog()
        SocketIO.emit.assert_called()
        
    def test_send_party(self):
        SocketIO.emit = MagicMock()
        Integration.send_party()
        SocketIO.emit.assert_called()
