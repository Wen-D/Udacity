import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def play_game():
    item = []
    option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    intro(item, option)
    field(item, option)


play_game()
