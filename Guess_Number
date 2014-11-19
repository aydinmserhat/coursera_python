# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

guesses = 0
secret_number = 0

# helper function to start and restart the game
def new_game():
    global guesses , secret_number
    secret_number = random.randrange(0,101)
    guesses = 7
    print 'New Game'
    print ''
    
   

# define event handlers for control panel
def range100():
    global guesses , secret_number
    secret_number = random.randrange(0,101)
    guesses = 7
    print 'range is from 0 up to 100'
    print "Number of remaining guesses is", guesses
    print ''
    # button that changes the range to [0,100) and starts a new game 
    

def range1000():
    global guesses , secret_number
    secret_number = random.randrange(0,1001)
    guesses = 10
    print 'range is from 0 up to 1000'
    print "Number of remaining guesses is", guesses
    print ''
    # button that changes the range to [0,1000) and starts a new game     
    
    
def input_guess(guess):
    global guesses , secret_number
    print "Guess was", guess
    if int(guess) < secret_number and guesses > 0:
        guesses = guesses - 1
        print "Higher!"
        print "Number of remaining guesses is", guesses
        print ""
    elif int(guess) > secret_number and guesses > 0:
        guesses = guesses - 1
        print "Lower!"
        print "Number of remaining guesses is", guesses
        print "" 
    elif int(guess) == secret_number:
        print "Correct!"
        print ''    
    if guesses == 0:
        print "Sorry you ran out of guesses. The number was", secret_number
        print ''   
        new_game()    

# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements
frame.add_button('restart' , new_game , 200)
frame.add_button("Range is (0, 100)", range100, 200)
frame.add_button("Range is (0, 1000)", range1000, 200)
frame.add_input("Please Enter A Guess:", input_guess, 150)

# Starts the game
range100()

# start frame
frame.start()


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
