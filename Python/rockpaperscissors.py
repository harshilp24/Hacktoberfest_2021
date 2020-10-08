""" I will be attempting to create a rock, paper, scissors game against the AI
Rules are as of follows:
Scissors beat Paper
Paper beats Rock
Rock beats Scissors"""

#importing the required modules
import pyinputplus as pyip
import random

# To start, I will find out how to address the player

print ("Welcome to a game of rock, paper, scissors. How may I address you?")
user_name = pyip.inputStr()

# Creating a count for wins
user_winscount = 0
# Creating a count for games played
games_played = 0

while True:
    # Ask user to input his move
    print (user_name + ", what is your move?")
    user_move = pyip.inputMenu(['rock', 'paper', 'scissors'])

    # Generating a random move by the AI
    AI_RandomGeneratedNumber = random.randint(1,3)
    if AI_RandomGeneratedNumber == 1:
        AI_move = 'rock'
    elif AI_RandomGeneratedNumber == 2:
        AI_move = 'paper'
    elif AI_RandomGeneratedNumber == 3:
        AI_move = 'scissors'



    # Determining the winner

    # Draw Condition
    if user_move == AI_move:
        print ("It's a tie")

    # User Wins Condition
    elif (user_move == 'rock' and AI_move == 'scissors' or
    user_move == 'paper' and AI_move == 'rock'
    or user_move == 'scissors' and AI_move == 'paper'):
        print (user_name + " wins!")
        user_winscount += 1

    # AI Wins Condition
    else:
        print (user_name + " lost!")

    # Calculating the counter
    games_played += 1
    print (user_name + ", you've won " + str(user_winscount) + " games out of " + str(games_played) + ".")


    # Ask to try again
    print ("Try again?")
    tryagain_option = pyip.inputChoice(['Y', 'N'])

    if tryagain_option == 'Y':
        continue
    elif tryagain_option == 'N':
        print ("It was fun playing with you! Goodbye")
        break

