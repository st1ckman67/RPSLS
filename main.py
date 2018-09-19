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

win_message = {'scissors':{2:' cuts paper', 3:' decapitates lizard', 4:' eats paper'},
                'paper':{0:' covers rock', 1:' disproves Spock'},
                'rock':{3:' crushes lizard', 4:' crushes scissors'},
                'lizard':{1:' poisons Spock', 2:' eats paper'},
                'Spock':{0:' vaporizes rock', 4:' smashes scissors '}}


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
    a = win_message[winner][loser]

    print(winner + a)


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
        print_win(player_choice, comp_number)
        print("Player wins!")        
    else:
        print_win(comp_choice, player_number)
        print("Computer wins!")

    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
