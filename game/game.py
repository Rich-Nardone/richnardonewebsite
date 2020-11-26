"""
    Handles most of the game logic
"""

# local imports
from .game_io import progress, prompt_in, send_out
from .scenario import scenario, start_scenario

# should probably read prompts from another file...
# fix this in all the scenarios

# COMBAT COMBAT COMBAT
def combat(player, enemy):
    send_out("Player "+player.id+" begins combat with "+enemy.id)
    send_out("Player "+player.id+" starts at "+str(player.health)+"/"+str(player.max_health))
    send_out("Player "+enemy.id+" starts at "+str(enemy.health)+"/"+str(enemy.max_health))
    while not player.is_dead() and not enemy.is_dead():
        # Prompt player aciton
        action = prompt_in()
        # Determine faster speed, Pokemon style
        if enemy.speed > player.speed:
            # Enemies go first
            send_out(enemy.attack('melee',player))
            if "attack" in action:
                send_out(player.attack("melee",enemy))
            else:
                continue # we don't handle other actions right now
        else:
            # players go first
            if "attack" in action:
                send_out(player.attack("melee",enemy))
                send_out(enemy.attack('melee',player))
            else:
                continue # we don't handle other actions right now
    winner = player.id
    if player.is_dead():
        winner = enemy.id
    send_out("Combat has ended! "+winner+" has won!")

def game(user):
    """ Runs the game, given a user """
    # player character
    player = start_scenario(user)
    progress(user, player, "start")
    # this tuple is shaped: "Player, String" where string is the area
    state_tuple = scenario(player, "intro")
    while state_tuple[1] != "end":
        progress(user, state_tuple[0], state_tuple[1])
        state_tuple = scenario(state_tuple[0], state_tuple[1])
    print("game has reached endstate")
    return user
