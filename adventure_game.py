

# You can use this workspace to write and submit your adventure game project.

import time
import random
def message_pause(msg):
    print (msg)
    time.sleep(3)
    
def start(item, option):
    #
    message_pause("You find yourself in the middle of France"
                "with only two coins in your pocket\n")
    message_pause("You see a billboard with " + option + " advertising a sale at the nearest mall"
                "everybody seems to be walking in that direction.\n")
    message_pause("In front of you you see a bakery\n")
    message_pause("To your left you see a taxi driver.\n")
    
def action1(item, option):
    # 
    message_pause("Enter 1 to buy bread.\n")
    message_pause("Enter 2 to take a taxi to the nearest mall.\n")
    message_pause("What would you like to do?\n")
    message_pause("(Please enter 1 or 2.)\n")
    while True:
        action_one = input("Please enter 1 or 2.")
        if action_one == "1":
            bakery(item, option)
            break
        elif action_one == "2":
            mall(item, option)
            break

def bakery(item, option):
    # Things that happen to the player in the bakery 
    message_pause("You smeel the bread and decide to go to the bakery.\n")
    message_pause("as you approach the bakery, you see " + option + ".\n")
    message_pause("You feel embarrased that " + option + "might see you at the bakery!")
    message_pause( option + " waves you!\n")
    message_pause("You pretend you don't see him.\n")
    if "sunglasses" not in item :
        message_pause("You search for your sunglasses")
    action_two = input("Would you like to (1) stay or (2) step out?\n")
    while True:
        if action_two == "1":
            ice_cream(item, option)
            break
        elif action_two == "2":
            step_out(item, option)
            break

def ice_cream(item, option):
    # Things that happen when the player gets ice_creams  
    if "sunglasses" not in item:
        message_pause("You stay and buy an ice cream\n")
        message_pause("Before heading out you say hi to " + option + ".\n")
        message_pause("Without your sunglassses you cannot hide!\n")
        play_again()
    else:    
        message_pause("As the " + option + "moves to attack, you unsheath your new sunglasses.\n")
        message_pause("The sunglasses of Ogoroth shines brightly in your hand as you brace yourself for the attack.\n")
        message_pause("But the " + option + " takes one look at your shiny new toy and runs away!\n")
        message_pause("You have rid the town of the " + option + ". You are victorious!\n")
        play_again()

def step_out(item, option):
    message_pause("You step out and walk around the block.")
    action1(item ,option)

def mall(item, option):
    # Things that happen to the player goes in the mall 
    if "sunglasses" in item:
        message_pause("you wear your sunglasses but decide they look outdated")
        item.append("sunglasses")
        action1(item ,option)
    else:
        message_pause("You decide to buy a new pair of pants.")
        action1(item ,option)

def play_again():
    playAgain = input("Would you like to play again? (y/n)").lower()
    while True:
        if playAgain == 'y':
            message_pause("Excellent! Restarting the game ...")
            play_game()
            break

        elif playAgain == 'n':
            message_pause("Thanks for playing. See you next time.")
            break

def play_game():
    item = []
    option = random.choice(["Oprah","gym instructor","your mother","school teacher","anti-christ"])

    start(item,option)
    action1(item,option)


play_game() 
