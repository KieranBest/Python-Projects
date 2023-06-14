#Starting code came from 
#https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

#importing the time module
import time
import random

#difficulty levels
easyWords = ["must","lord","limp","duke","rage","name","raft","mute","tide","slug"]
mediumWords = ["racing","losing","accuse","fabric","squawk","uphold","slider","amidst","manage","thrust"]
hardWords = ["offended","oblivion","digested","drumbeat","discrete","hindered","meditate","haystack","draining","mourning"]

#array for storing previous guesses
previousGuesses = []

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name)

#wait for 1 second
time.sleep(1)

#determines the difficulty along with the word
difficulty = input("What difficulty would you like to play? (easy, medium, hard) ")
if difficulty == "easy":
    word = easyWords[random.randint(0,9)]
elif difficulty == "medium":
    word = mediumWords[random.randint(0,9)]
elif difficulty == "hard":
    word = hardWords[random.randint(0,9)]

print ("You have chosen " + difficulty + " difficulty.")

#wait for 1 second
time.sleep(1)

print("Time to play hangman!")

print ("Start guessing...")
time.sleep(0.5)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash
            print ("_",end=""),     
       
        # and increase the failed counter with one
            failed += 1    


    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("\nYou won")
    # exit the script
        break            

    #if user has input guesses, print them out
    if len(previousGuesses) > 0:
        print("\nPrevious guesses: ", *previousGuesses)

    # ask the user go guess a character
    guess = input("guess a character:") 
    previousGuesses.append(guess)

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose"  )
            print ("The word was " + word)
