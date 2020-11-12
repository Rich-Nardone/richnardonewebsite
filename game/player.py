"""
    Container for player stats
"""

class Player:
    """ Class for player stats and data """

    def __init__(self):
        self.id = "name"
        self.gen = "gender"
        # stats
        # Strength: Used for slapping and stronging things
        self.str = 0
        # Dexterity: Used for going fast and being fast
        self.dex = 0
        # Constitution: Healthiness and not-die ability
        self.con = 0
        # Intelligence: The BIG BRAIN
        self.int = 0
        # Charisma: How likeable or punchable you are
        self.cha = 0
        # Luck: Lucky you, huh?
        self.luk = 0
        # totals
        # Health: Your life.
        self.max_health = 100 + self.con*10
        self.health = self.max_health
        # Mana: Magic is a thing?
        self.max_mana = self.int*5
        self.mana = 0
        # money
        self.money = self.luk*5
    
    def is_dead(self):
        """ Has the player died? """
        return self.health <= 0
    
    def damage(self, dmg_rcv):
        """ Player receives damage """
        self.health -= dmg_rcv
        if self.is_dead():
            return True # trigger death stuff
        return None # return nothing