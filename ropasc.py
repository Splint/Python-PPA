"""
Filename:   ropasc.py
Author:     Sang Shin
Date:       08/14/2012
"""
#!/bin/env python
import sys
import random

CONSTANT_ROCK = "rock"
CONSTANT_SCISSORS = "scissors"
CONSTANT_PAPER = "paper"

USER_WIN_COUNT = 0
COMP_WIN_COUNT = 0
TIE_COUNT = 0

USER_CHOICE = []
COMP_CHOICE = {"rock":"paper",
               "paper":"scissors",
               "scissors":"rock"}

def printSummary():
    global USER_WIN_COUNT, COMP_WIN_COUNT, TIE_COUNT

    print "---------- Summary ----------"
    print "Player Wins: %d" % int(USER_WIN_COUNT)
    print "Computer Wins: %d" % int(COMP_WIN_COUNT)
    print "Tie: %d" % int(TIE_COUNT)
    print
    print "Thank you for playing"

def printGame(userInput, compInput, user_state):
    if user_state == "tie":
        print "%s vs. %s ... it's a tie!" % (str(userInput), str(compInput))

    elif user_state == "win":
        print "%s vs. %s ... you win!" % (str(userInput), str(compInput))

    elif user_state == "lose":
        print "%s vs. %s ... you lose!" % (str(userInput), str(compInput))

    else:
        print "An error has occurred. Exiting."
        sys.exit()

def getCompResponse(arr):
    rand_choices = {0:"rock",
                    1:"paper",
                    2:"scissors"}
    """
    If the USER_CHOICE list contains less than 5 elements, we do random picking.
    """
    if len(arr) < 5:
        rand_num = random.randrange(0, 3)
        return rand_choices[rand_num]
        
    """
    If the USER_CHOICE list contains 5 or more elements, we add a bit of small AI to the
    computer's choices.
    """
    user_rock_count = arr.count("rock")
    user_paper_count = arr.count("paper")
    user_scissors_count = arr.count("scissors")

    if (user_rock_count > user_paper_count) and (user_rock_count > user_scissors_count):
        return COMP_CHOICE["rock"]
        
    if (user_paper_count > user_rock_count) and (user_paper_count > user_scissors_count):
        return COMP_CHOICE["paper"]
        
    if (user_scissors_count > user_rock_count) and (user_scissors_count > user_paper_count):
        return COMP_CHOICE["scissors"]
    
    rand_num = random.randrange(0, 3)
    return COMP_CHOICE[rand_choices[rand_num]]

def startGame(userInput):
    global USER_WIN_COUNT, COMP_WIN_COUNT, TIE_COUNT

    USER_CHOICE.append(userInput)
    comp_rep = getCompResponse(USER_CHOICE)

    if str(userInput) == "rock":
        if comp_rep == "rock":
            printGame(userInput, comp_rep, "tie")
            TIE_COUNT += 1

        if comp_rep == "paper":
            printGame(userInput, comp_rep, "lose")
            COMP_WIN_COUNT += 1

        if comp_rep == "scissors":
            printGame(userInput, comp_rep, "win")
            USER_WIN_COUNT += 1

    if str(userInput) == "paper":
        if comp_rep == "rock":
            printGame(userInput, comp_rep, "win")
            USER_WIN_COUNT += 1

        if comp_rep == "paper":
            printGame(userInput, comp_rep, "tie")
            TIE_COUNT += 1

        if comp_rep == "scissors":
            printGame(userInput, comp_rep, "lose")
            COMP_WIN_COUNT += 1 

    if str(userInput) == "scissors":
        if comp_rep == "rock":
            printGame(userInput, comp_rep, "lose")
            COMP_WIN_COUNT += 1

        if comp_rep == "paper":
            printGame(userInput, comp_rep, "win")
            USER_WIN_COUNT += 1

        if comp_rep == "scissors":
            printGame(userInput, comp_rep, "tie")
            TIE_COUNT += 1

def main():
    """
    The following is the procedure of the algorithm this program takes.
    
    * The program should loop until the user types in "q" or "Q".
        - "Quit" will be an enhancement to the program
    * The program needs to error check to see if the user correctly puts in a string
        - Otherwise, the loop continues for a valid input
    * 
    """
    while True:
        userInput = raw_input("Enter a choice (q or Q to quit): ")

        if (str(userInput).lower() == "q") or (str(userInput).lower() == "quit"):
            printSummary()
            sys.exit()
        
        if (str(userInput).lower() == "r") or (str(userInput).lower() == "rock"):
            userInput = "rock"
            startGame(userInput)
            
        elif (str(userInput).lower() == "p") or (str(userInput).lower() == "paper"):
            userInput = "paper"
            startGame(userInput)
        
        elif (str(userInput).lower() == "s") or (str(userInput).lower() == "scissors"):
            userInput = "scissors"
            startGame(userInput)
        
        else:
            print "An invalid response was enter. Try again."
       
     
if __name__ == "__main__":
    main()
