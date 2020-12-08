"""
    Loading and running every scenario
"""

# local imports
from .game_io import prompt_in, send_out
from .player import Player

# START
def start_scenario(user=None):
    """ Tries to find a player for the user, otherwise creates new """
    start_text = "You are in a white, bare room with nothing but a mirror with a few words on it."
    start_text = (
        start_text
        + "Upon further inspection the mirror seems to be asking you a question, “Who are you?”"
    )
    send_out(start_text)
    # character creation
    player = Player()
    # TODO fetch player info for user 'user' from the database need player name, gender and class
    return player

def scenario(player, scenario_id):
    """ Loads into the scenario """
    if scenario_id == "intro":
        send_out(
            "You wake up at your desk in class, with no one in sight. Strangely enough, "
            + "it looks like everyone has left only recently and forgotten their things."
        )
        action = prompt_in()
        looted = False
        while action:
            if "loot" in action or "steal" in action:
                if not looted:
                    send_out("You find $20 in people's bags.")
                    player.money += 20
                    looted = True
                else:
                    send_out("You've already looted everything!")
            if "look" in action:
                send_out("It seems dark outside...")
            if "leave" in action:
                send_out("You leave the room.")
                return (player, "intro_hall")
            action = prompt_in()
    if scenario_id == "intro_hall":
        send_out(
            "As you leave the room, you notice that the hallway is empty as well,"
            + "with some strange gray trails all heading either towards or from the main entrance."
        )
        send_out("Where do you go?")
        action = prompt_in()
        next_area = None
        while not next_area:
            if "classroom" in action or "away" in action:
                next_area = "classroom"
                break
            if "entrance" in action or "towards" in action:
                next_area = "entrance"
                break
            action = prompt_in()
        send_out(
            "As you approach, there is a slow and constant squishing sound,"
            + "like the noises of an oversaturated bath towel."
        )
        return (player, next_area)
    if scenario_id == "classroom":
        send_out(
            "Peeking in, you find a strange gray mass that rests on top of the trail. The stra"
            + "nger thing is that the room itself seems to lack color wherever this mass goes."
        )
        action = prompt_in()
        while action:
            if "fight" in action:
                send_out("You begin combat with the gray slime!")
                # Changes in combat-and-death branch
            if "leave" in action:
                return (player, "entrance")
    return (player, scenario_id)
