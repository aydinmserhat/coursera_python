# Rock-paper-scissors-lizard-Spock
# Can be played @ the following url
# http://www.codeskulptor.org/#user10_HNWUT17pvi_10.py
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
# helper functions
def number_to_name(choiceNum):
# fill in your code below
# convert number to a name using if/elif/else
    if choiceNum == 0:
        choiceNum = "rock"
        return choiceNum
    elif choiceNum == 1:
        choiceNum = "Spock"
        return choiceNum
    elif choiceNum == 2:
        choiceNum = "paper"
        return choiceNum
    elif choiceNum == 3:
        choiceNum = "lizard"
        return choiceNum
    elif choiceNum == 4:
        choiceNum = "scissors"
        return choiceNum
    else:
        print "Output not within normal parameters, BAZINGA"
# don't forget to return the result!
def name_to_number(choiceName):
# fill in your code below
# convert name to number using if/elif/else
    if choiceName == "rock":
        choiceName = 0
        return choiceName
    elif choiceName == "Spock":
        choiceName = 1
        return choiceName
    elif choiceName == "paper":
        choiceName = 2
        return choiceName
    elif choiceName == "lizard":
        choiceName = 3
        return choiceName
    elif choiceName == "scissors":
        choiceName = 4
        return choiceName
    else:
        print "Input not within normal parameters, BAZINGA"
# don't forget to return the result!
def rpsls(name):
# fill in your code below
# convert name to player_number using name_to_number
    player_number = name_to_number(name)
#print player_number
# compute random guess for comp_number using random.randrange
    comp_number = random.randrange(0,5)
#print comp_number
# compute difference of player_number and comp_number modulo five
# use if/elif/else to determine winner
    if (player_number - comp_number) % 5 >= 3:
        winner = "Computer wins!"
    elif (player_number - comp_number) % 5 == 0:
        winner = "Player and computer tie!"
    else:
        winner = "Player wins!"
# convert comp_number to name using number_to_name
    compChoice = number_to_name(comp_number)
# print results
    print "Player chooses " + name
    print "Computer chooses " + compChoice
    print winner
    print("\r\n")
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric
