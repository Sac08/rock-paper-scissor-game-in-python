#from coursera:Interactive Programming In Python;Rice University
CODE==>
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else :
        return "ERROR"
    


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"
    
def rpsls(player_choice): 
    print 
    print "player chooses " + player_choice
    player_number=name_to_number(player_choice)	
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print "computer chooses "+ comp_choice
    winner=(comp_number - player_number)%5
    if winner<=2 and winner>0:
        print "computer wins!"
    elif winner>=2:
        print "player wins!"
    else:
        print "player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


