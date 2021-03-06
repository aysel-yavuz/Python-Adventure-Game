import time

import random

import sys


# 1 sec pause is made after the text is appeared
def print_pause(message):
    print(message)
    time.sleep(1)

# Description for the player of what is happening in the game
def intro():
    print_pause("You are in a small village during Halloween "
                "early in the evening.")
    print_pause("It's getting darker and more dangerous outside.")
    print_pause("Your goal is to safely reach home on the other side of "
                "the village.")

# Validation of the player's input
def valid_input(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option in response:
                response = option
                return response
        print_pause("Sorry, this isn't on the list")

        
# Different scenarios based on the previous choice in case 
# the player meets trick-or-treaters
def trick_or_treaters(item, play_again_list):
    if item == "candies":
        print_pause("Candies made the trick-or-treaters very happy.")
        print_pause("They let you continue your way.")
    else:
        if item == "Waterguns":
            print_pause("Your waterguns scared the trick-or-treaters and "
                        "made them cry.")
        elif item == "garlic":
            print_pause("Garlic isn't something trick-or-treaters expect "
                        "to get at Halloween!. It only made them cry.")
        print_pause("Their parents kicked you out of the village.")
        print_pause("You lost! You didn't manage to reach your home.")
        play_again(play_again_list)


# Different scenarios based on the previous choice in case
# the player meets zombies
def zombies(item, play_again_list):
    if item == "waterguns":
        print_pause("With your waterguns you shot directly to zombies.")
        print_pause("All zombies died! You may continue your way.")
    elif item == "candies" or item == "garlic":
        print_pause("This is not work on zombies!")
        print_pause("You lost! You've also become a zombie and "
                    "you won't go back home.")
        play_again(play_again_list)

        
# Different scenarios based on the previous choice in case
# the player meets vampires
def vampires(item, play_again_list):
    if item == "garlic":
        print_pause("You detered the vampires with garlic.")
        print_pause("All vampires escaped! You may continue your way.")
    elif item == "candies" or item == "waterguns":
        print_pause("This is not work on vampires!")
        print_pause("You lost! You've also become a vampire and "
                    "you won't go back home.")
        play_again(play_again_list)

# The player uses the item in their bag against the enemy
def action_1(enemy, item, items_trunk, play_again_list, enemies):
    # Enemies are not repeating during one game   
    enemies.remove(enemy)
    if enemy == "trick-or-treaters":
        trick_or_treaters(item, play_again_list)
    elif enemy == "zombies":
        zombies(item, play_again_list)
    elif enemy == "vampires":
        vampires(item, play_again_list)
    print_pause("Your bag is empty again.")
    items_trunk.append(item)

    
# The player exchanges the item in the bag
def action_2(enemy, item, items_trunk, play_again_list, enemies):
    print_pause("You are back at the old trunk.")
    print_pause("Which item do you want to exchange item for?\n")
    items_trunk.append(item)
    print_pause(" - waterguns\n"
                " - garlic\n")
    item = valid_input("Please, enter a name of the item.\n", items_trunk)
    print_pause("You put watergun in your bag and return to the enemy")
    items_trunk.remove(item)
    action_1(enemy, item, items_trunk, play_again_list, enemies)

    
# The players finds a trunk and has to pick an item from
# the ["candies", "waterguns", "holy water"] list
def find_trunk(items_trunk):
    print_pause("Further on your way, you find an old trunk with "
                "three items in it.")
    print_pause("However, only one item can suit into your bag.")
    print_pause("Which item would you like to take?\n")
    print_pause(" - candies\n"
                " - waterguns\n"
                " - garlic\n")
    item = valid_input("Please, enter a name of the item.\n", items_trunk)
    print_pause("You put item in your bag and continue your way.")
    items_trunk.remove(item)
    return item


# The player is given a choice of two actions after meeting an enemy:
# to use an item against the enemy
# or to return to the trunk and pick another item.
def meet_enemy(item, items_trunk, actions, play_again_list, enemies):
    # Enemy is chosen in a random order    
    enemy = random.choice(enemies)
    print_pause("Suddenly, you've been approached by a bunch of enemy.")
    print_pause("What's your next step?\n")
    print_pause(" 1. Get your item out of the bag.\n"
                " 2. Run back to the old trunk to exchange your item.\n")
    action = valid_input("Please enter a number 1 or 2.\n", actions)
    if action == '1':
        action_1(enemy, item, items_trunk, play_again_list, enemies)
    elif action == '2':
        action_2(enemy, item, items_trunk, play_again_list, enemies)


# After the game is over, the user can play the game again
def play_again(play_again_list):
    print_pause("Would you like to play again?")
    response = valid_input("Please, enter yes or no.\n", play_again_list)
    if response == "yes":
        print_pause("Excellent! Restarting the game...\n")
        play_game()
    elif response == "no":
        sys.exit()


def game_body(items_trunk, enemies, actions, play_again_list):
    while len(enemies) != 0:
        item = find_trunk(items_trunk)
        meet_enemy(item, items_trunk, actions, play_again_list, enemies)
    print_pause("Congratulatons!")
    print_pause("You defeated all enemies and safely reached your home!")
    play_again(play_again_list)


def play_game():
    items_trunk = ["candies", "waterguns", "garlic"]
    enemies = ["trick-or-treaters", "zombies", "vampires"]
    actions = ['1', '2']
    play_again_list = ["yes", "no"]
    intro()
    game_body(items_trunk, enemies, actions, play_again_list)


play_game()
