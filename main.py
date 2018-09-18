import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors

win_message = {'scissors':['', '', ' cuts paper', '', 'eats paper', ''],
                'paper':[' covers rock', ' disproves Spock'],
                'rock':['', '', '', ' crushes lizard', ' crushes scissors'],
                'lizard':['', ' poisons Spock', ' eats paper'],
                'Spock':[' vaporizes rock', '', '', '', ' smashes scissors ']}


# helper functions
def name_to_number(name):
    # convert name to number
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    else:
        number = 4
    return number   
 

def number_to_name(number):
    # convert number to a name
    if number == 0 :
        name = 'rock'
    elif number == 1 :
        name = 'Spock'
    elif number == 2 :
        name = 'paper'
    elif number == 3 :
        name = 'lizard'
    else:
        name = 'scissors'
    return name


def print_win(winner, loser):    
    a = win_message.get(winner)
    b = name_to_number(loser)
    print(winner + a[b])


def rpsls(player_choice): 
    # print out the message for the player's choice
    print("\nPlayer chooses " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print("Computer chooses " + comp_choice)

    # compute difference of comp_number and player_number modulo five
    result = (player_number - comp_number) % 5

    # determine winner, print winner message
    if result == 0:
        print("It's a tie")
    elif result in range(1,3) :
        print_win(player_choice, comp_choice)
        print("Player wins!")        
    else:
        print_win(comp_choice, player_choice)
        print("Computer wins!")

    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
