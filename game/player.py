"""
    Container for player stats
"""

class Player:
    """ Class for player stats and data """

    def __init__(self):
        self.id = "name"
        # health
        self.health = 100
        # stats
    
    def is_dead(self):
        """ Has the player died? """
        return self.health <= 0
    
    def damage(self, dmg_rcv):
        """ Player receives damage """
        self.health -= dmg_rcv
        if self.is_dead():
            return True # trigger death stuff
        return None # return nothing