"""
    Container for player stats
"""


class Player:
    """ Class for player stats and data """

    def __init__(self):
        self.id = "name"
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
        self.max_health = 100 + self.con * 10
        self.health = self.max_health
        # Mana: Magic is a thing?
        self.max_mana = self.int * 5
        self.mana = 0
        # money
        self.money = self.luk * 5
        self.gen = "gender"
        self.character_class = "class"
        self.checkpoint = "start"

    def is_dead(self):
        """ Has the player died? """
        return self.health <= 0

    def damage(self, dmg_rcv):
        """ Player receives damage """
        self.health -= dmg_rcv
        if self.is_dead():
            return True  # trigger death stuff
        return None  # return nothing

    def make_neet(self):
        """ Create 'neet' archetype character. """
        # Strength: Used for slapping and stronging things
        self.str = 65
        # Dexterity: Used for going fast and being fast
        self.dex = 80
        # Constitution: Healthiness and not-die ability
        self.con = 50
        # Intelligence: The BIG BRAIN
        self.int = 75
        # Charisma: How likeable or punchable you are
        self.cha = 70
        # Luck: Lucky you, huh?
        self.luk = 50
        # totals
        # Health: Your life.
        self.max_health = 100 + self.con * 10
        self.health = self.max_health
        # Mana: Magic is a thing?
        self.max_mana = self.int * 5
        # money
        self.money = self.luk * 5

    def make_bookworm(self):
        """ Create 'bookworm' archetype character. """
        # Strength: Used for slapping and stronging things
        self.str = 35
        # Dexterity: Used for going fast and being fast
        self.dex = 75
        # Constitution: Healthiness and not-die ability
        self.con = 80
        # Intelligence: The BIG BRAIN
        self.int = 90
        # Charisma: How likeable or punchable you are
        self.cha = 25
        # Luck: Lucky you, huh?
        self.luk = 60
        # totals
        # Health: Your life.
        self.max_health = 100 + self.con * 10
        self.health = self.max_health
        # Mana: Magic is a thing?
        self.max_mana = self.int * 5
        # money
        self.money = self.luk * 5

    def make_jock(self):
        """ Create 'jock' archetype character. """
        # Strength: Used for slapping and stronging things
        self.str = 90
        # Dexterity: Used for going fast and being fast
        self.dex = 40
        # Constitution: Healthiness and not-die ability
        self.con = 20
        # Intelligence: The BIG BRAIN
        self.int = 35
        # Charisma: How likeable or punchable you are
        self.cha = 50
        # Luck: Lucky you, huh?
        self.luk = 50
        # totals
        # Health: Your life.
        self.max_health = 100 + self.con * 10
        self.health = self.max_health
        # Mana: Magic is a thing?
        self.max_mana = self.int * 5
        # money
        self.money = self.luk * 5
