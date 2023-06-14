#Starting code came from 
#https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

#import required modules
from game import playGame
from game import playAgainFunct
import time

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name)

#wait for 1 second
time.sleep(1)

playGame()

#wait for 1 second
time.sleep(1)

while True:
    playAgainFunct()