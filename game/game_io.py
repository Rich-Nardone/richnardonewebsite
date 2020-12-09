"""
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""
import inspect
import os
import sys
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from settings import socketio
import user_input

user_in = user_input.UserInput()


def prompt_in():
    """ Method for receiving input """
    text = user_in.read_input()
    while not text:
        time.sleep(0.05)  # wait for 50 milliseconds
        text = user_in.read_input()
    return text


def send_out(msg):
    """ Method for sending reply """
    socketio.emit("chatlog updated", {"text": msg})
