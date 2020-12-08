"""
    A class for users which streamlines player object retrieval
"""
import models


class User:
    """ A class which links a user to their email (hidden from all users) """

    def __init__(self, email):
        self.email = email
        self.user_id = None
        self.selected_character_id = None
        self.character_counter = 0
        for model in models.db.session.query(models.username.id).filter(
            models.username.email == email
        ):
            self.user_id = model[0]

        if self.user_id:
            self.char_list = []
            for model in models.db.session.query(models.character).filter(
                models.character.user_id == self.user_id
            ):
                self.char_list.append(model)
            self.character_counter = len(self.char_list)

    def user_exists(self):
        """ Check if user exists """
        if self.user_id:
            return True
        return False

    def get_characters(self):
        """ Gets the characters for the user """
        display_list = []
        for char in self.char_list:
            info = {}
            info["id"] = char.id
            info["character_name"] = char.character_name
            info["class"] = char.character_class
            display_list.append(info)
        return display_list

    def char_select(self, char_id):
        """ Selects a character for the user """
        self.selected_character_id = char_id

    def get_inventory(self):
        """ Gets the player's inventory for current character """
        inventory_list = []
        for x in models.db.session.query(models.inventory).filter(
            models.inventory.character_id == self.selected_character_id
        ):
            inventory_list.append(x.items)
        return inventory_list
