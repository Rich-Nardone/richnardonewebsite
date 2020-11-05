"""
    TODO :
    - use socket.io for prompt_in and send_out
    - include PSQL additions, likely in another method
        called report_progress
"""

def prompt_in():
    """ Method for receiving input """
    text = input()
    return text

def send_out(msg):
    """ Method for sending reply """
    print(msg)