"""
    Loading and running every scenario
"""

# local imports
from .game_io import prompt_in, send_out
from .player import Player


def scenario(player, scenario_id):
    """ Loads into the scenario """
    if scenario_id == "start":
        send_out(
            "You are in a white, bare room with nothing but a mirror with a few words on it."
            + "Upon further inspection the mirror seems to be asking you a question, “Who are you?”",
            player.id,
        )
        return (player, "intro", player.id)
    if scenario_id == "intro":
        send_out(
            "You wake up at your desk in class, with no one in sight. Strangely enough, "
            + "it looks like everyone has left only recently and forgotten their things.",
            player.id,
        )
        action = prompt_in()
        looted = False
        while action:
            if parse(action)["loot"]:
                if not looted:
                    send_out("You find $20 in people's bags.", player.id)
                    player.money += 20
                    looted = True
                else:
                    send_out("You've already looted everything!", player.id)
            if parse(action)["look"]:
                send_out("It seems dark outside...", player.id)
            if parse(action)["leave"]:
                send_out("You leave the room.", player.id)
                return (player, "intro_hall", player.id)
            action = prompt_in()
    if scenario_id == "intro_hall":
        send_out(
            "As you leave the room, you notice that the hallway is empty as well,"
            + "with some strange gray trails all heading either towards or from the main entrance.",
            player.id,
        )
        send_out("Where do you go?", player.id)
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
            + "like the noises of an oversaturated bath towel.",
            player.id,
        )
        return (player, next_area, player.id)
    if scenario_id == "classroom":
        send_out(
            "Peeking in, you find a strange gray mass that rests on top of the trail. The stra"
            + "nger thing is that the room itself seems to lack color wherever this mass goes.",
            player.id,
        )
        action = prompt_in()
        slime_alive = True
        while action:
            if parse(action)["fight"] and slime_alive:
                send_out("You begin combat with the gray slime!", player.id)
                slime_npc = Player("", 10, 10, 10, 0, 0, 0)
                combat(player, slime_npc, player.id)
                slime_alive = False
            if parse(action)["leave"]:
                return (player, "entrance", player.id)
    if scenario_id == "entrance":
        send_out(
            "Outside of the schoool, you find a few of your classmates and your professor, trying "
            + "to fend off some colorless slimes with brooms.",
            player.id,
        )
        action = prompt_in()
        slime_alive = True
        looted = False
        while action:
            if parse(action)["fight"]:
                send_out("You begin combat with the gray slimes!", player.id)
                slime_npc1 = Player("", 10, 10, 10, 0, 0, 0)
                combat(player, slime_npc1, player.id)
                slime_npc2 = Player("", 10, 10, 10, 0, 0, 0)
                combat(player, slime_npc2, player.id)
                slime_npc3 = Player("", 10, 10, 10, 0, 0, 0)
                combat(player, slime_npc3, player.id)
                slime_alive = False
            if parse(action)["talk"]:
                send_out(
                    "You walk over and see your classmates wearily pushing the slimes away."
                    + ' "Oh, you\'re alive!", goes your professor. "Come lend us a hand!"',
                    player.id,
                )
            if parse(action)["loot"] and not looted:
                send_out("You find a broom!", player.id)

    return (player, scenario_id, player.id)


def parse(command):
    """
    function that parses a string and returns a map of strings->booleans based on command
    - command is a string
    """
    d = {}

    # exploration
    d["fight"] = "fight" in command or "attack" in command
    d["leave"] = "leave" in command
    d["look"] = "look" in command
    d["loot"] = "loot" in command or "steal" in command
    d["talk"] = "talk" in command
    # fighting
    d["attack"] = "attack" in command
    d["melee"] = "melee" in command
    d["range"] = "range" in command
    d["magic"] = "magic" in command

    return d


# COMBAT COMBAT COMBAT
def combat(player, enemy):
    """ Simulates combat between the player and the enemy """
    send_out("Player " + player.id + " begins combat with " + enemy.id, player.id)
    send_out(
        "Player "
        + player.id
        + " starts at "
        + str(player.health)
        + "/"
        + str(player.max_health),
        player.id,
    )
    send_out(
        "Player "
        + enemy.id
        + " starts at "
        + str(enemy.health)
        + "/"
        + str(enemy.max_health),
        player.id,
    )
    while not player.is_dead() and not enemy.is_dead():
        # Prompt player aciton
        action = prompt_in()
        # Determine faster speed, Pokemon style
        if enemy.speed > player.speed:
            # Enemies go first
            send_out(enemy.attack("melee", player), player.id)
            if parse(action)["attack"]:
                send_out(player.attack("melee", enemy), player.id)
            else:
                continue  # we don't handle other actions right now
        else:
            # players go first
            if parse(action)["attack"]:
                send_out(player.attack("melee", enemy), player.id)
                send_out(enemy.attack("melee", player), player.id)
            else:
                continue  # we don't handle other actions right now
    winner = player.id
    if player.is_dead():
        winner = enemy.id
    send_out("Combat has ended! " + winner + " has won!", player.id)
