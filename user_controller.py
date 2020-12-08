import models

class User():
    def __init__(self, email): 
        self.email = email
        self.user_id = None
        self.selected_character_id = None
        self.character_counter = 0
        for x in models.db.session.query(models.username.id).filter(models.username.email == email): 
            self.user_id = x[0]
        
        if self.user_id: 
            self.char_list = []
            for z in models.db.session.query(models.character).filter(models.character.user_id == self.user_id): 
                self.char_list.append(z)
            self.character_counter = len(self.char_list)
    
    def user_exists(self): 
        if self.user_id: 
            return True
        return False
    
    def get_characters(self): 
        display_list = []
        for x in self.char_list: 
            info = {}
            info["id"] = x.id
            info["character_name"] = x.character_name
            info["class"] = x.character_class
            display_list.append(info)
        return display_list
    
    def char_select(self, char_id):
        self.selected_character_id = char_id
    
    def get_inventory(self):
        inventory_list = []
        for x in models.db.session.query(models.inventory).filter(models.inventory.character_id == self.selected_character_id):
            inventory_list.append(x.items)
        return inventory_list