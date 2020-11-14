"""
    Handles most of the game logic
"""

# local imports
from game_io import progress, prompt_in, send_out
from player import Player

# should probably read prompts from another file...
#  Marked with TODO story_file

# START
def start_scenario():
    # TODO story_file
    start_text = 'You are in a white, bare room with nothing but a mirror with a few words on it. Upon further inspection the mirror seems to be asking you a question, “Who are you?”'
    send_out(start_text)
    # character creation
    player = Player()
    return player

def scenario(player, scenario_id):
    # TODO story_file
    if scenario_id == 'intro':
        send_out("You wake up at your desk in class, with no one in sight. Strangely enough, it looks like everyone has left only recently and forgotten their things.")
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
                return (player, 'intro_hall')
            action = prompt_in()
    # TODO story_file
    if scenario_id == 'intro_hall':
        send_out("As you leave the room, you notice that the hallway is empty as well, with some strange gray trails all heading either towards or from the main entrance.")
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
        send_out("As you approach, there is a slow and constant squishing sound, like the noises of an oversaturated bath towel.")
        return (player, next_area)
    # TODO story_file
    if scenario_id == "classroom":
        send_out("Peeking in, you find a strange gray mass that rests on top of the trail. The stranger thing is that the room itself seems to lack color wherever this mass goes.")
        action = prompt_in()
        while action:
            if "fight" in action:
                send_out("You begin combat with the gray slime!")
                # TODO do combat
            if "leave" in action:
                return (player, "entrance")
    return (player, scenario_id)

def game(user):
    # player character
    player = start_scenario()
    progress(user, player, "start")
    # this tuple is shaped: "Player, String" where string is the area
    state_tuple = scenario(player, "intro")
    while state_tuple[1] != "end":
        progress(user, state_tuple[0], state_tuple[1])
        state_tuple = scenario(state_tuple[0], state_tuple[1])
    print("game has reached endstate")

#game('test')