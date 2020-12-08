"""
    Container for User Input
"""


class UserInput:
    """ Class to handle user input """

    def __init__(self):
        self.recent = ""
        self.updated = False

    def update(self, text):
        """ Updates most recent input """
        self.recent = text
        if not self.updated:
            self.updated = True

    def read_input(self):
        """ Tries to read input if there has been any new input """
        if self.updated:
            return self.recent
        return None
