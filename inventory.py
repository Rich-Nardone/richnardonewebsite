import models
from settings import db

def get_char():
    char = db.session.query(models.charlist).first()
    a = char.char
    return a

def item_sort_asc():
    """ sort inventory in ascending order and return """
    inventory = []
    # empties the "sorted" item table
    db.session.query(models.inventory_asc).delete()
    db.session.commit()
    # creates a dump of sorted values from the inventory table
    unsorted = db.session.query(models.inventory).order_by(models.inventory.items.asc())
    # loops through the dump and grabs all the items for the current character,
    #  adds them to the sorted items table
    for value in unsorted:
        sorted_item = models.inventory_asc(
            items=value.items, character_id=value.character_id
        )
        db.session.add(sorted_item)
        db.session.commit()
    """
    this key value is hard coded for now
    """
    key = get_char()
    personal_items = db.session.query(models.inventory_asc).filter_by(character_id=key)
    # currently this is just to print the sorted table as a test to make sure it works,
    #  in the future it should connect with front end to visually display the items sorted,
    #  probably best to send a list?
    for item in personal_items:
        inventory.append(item.item)
    return inventory


def item_sort_dsc():
    """ sort inventory in descending order and return it """
    inventory = []
    # empties the "sorted" item table
    db.session.query(models.inventory_dsc).delete()
    db.session.commit()
    # creates a dump of sorted values from the inventory table
    unsorted = db.session.query(models.inventory).order_by(
        models.inventory.items.desc()
    )
    # loops through the dump and grabs all the items for the current character,
    #  adds them to the sorted items table
    for value in unsorted:
        sorted_item = models.inventory_dsc(
            items=value.items, character_id=value.character_id
        )
        db.session.add(sorted_item)
        db.session.commit()
    """
    this key value is hard coded for now
    """
    key = get_char()
    personal_items = db.session.query(models.inventory_dsc).filter_by(character_id=key)
    # currently this is just to print the sorted table as a test to make sure it works,
    #  in the future it should connect with front end to visually display the items sorted,
    #  probably best to send a list?
    for item in personal_items:
        inventory.append(item.item)
    return inventory


def filter_by_type():
    """
    itemType is hard coded for now, should actually be fetched from front end. key is also hard coded, same as it is for item sort asc/dsc
    """
    itemType = "weapon"
    key = get_char()
    filtered_items = db.session.query(models.inventory).filter_by(
        item_type=itemType, character_id=key
    )

    for item in filtered_items:
        print(item.items)


def search_bar():
    """ produces a substring search of items in the inventory """
    items = db.session.query(models.inventory)
    search = "a"
    # this is a substring search function for the inventory,
    #  right now a is hardcoded but what should be done is
    #  fetching a search field and inserting it in as a variable
    for item in items:
        if search in item.items:
            print(item.items)


def show_inventory():
    """ returns an inventory array to display """
    # need to get character id from character selection page for load game
    key = get_char()
    dump = db.session.query(models.inventory).filter_by(character_id=key)
    inventory = []
    for item in dump:
        inventory.append(item.items)
    return inventory


def get_asc_inventory():
    """ getter for inventory in ascending order """
    return item_sort_asc()


def get_dsc_inventory():
    """ getter for inventory in descending order """
    return item_sort_dsc()


def get_user_inventory():
    """ getter for inventory (unordered) """
    return show_inventory()
