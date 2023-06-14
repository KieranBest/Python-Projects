#import required modules
import time
import random

#difficulty levels
easyWords = ["must","lord","limp","duke","rage","name","raft","mute","tide","slug"]
mediumWords = ["racing","losing","accuse","fabric","squawk","uphold","slider","amidst","manage","thrust"]
hardWords = ["offended","oblivion","digested","drumbeat","discrete","hindered","meditate","haystack","draining","mourning"]

global usedWords
usedWords = []
easyValue = [0]
mediumValue = [0]
hardValue = [0]

#determines the difficulty along with the word
def difficulty():
    global word 
    
    while True:
        difficulty = input("What difficulty would you like to play? (easy, medium, hard) ")
        if difficulty == "easy":
            word = easyWords[easyValue]
            for words in usedWords:
                if word == words:
                    easyValue = easyValue+1
                    word = easyWords[easyValue]
                    if easyValue == 9:
                        print("You have already played all of the easy words.", "\nYou have been moved to the next level.")
                        word = mediumWords[mediumValue]
                        difficulty = "medium"
            print ("You have chosen " + difficulty + " difficulty.")
            break
        elif difficulty == "medium":
            word = mediumWords[mediumValue]
            for words in usedWords:
                if word == words:
                    mediumValue = mediumValue+1
                    word = mediumWords[mediumValue]
                    if mediumValue == 9:
                        print("You have already played all of the medium words.", "\nYou have been moved to the next level.")
                        word = hardWords[hardValue]
                        difficulty = "hard"
            print ("You have chosen " + difficulty + " difficulty.")
            break
        elif difficulty == "hard":
            word = hardWords[hardValue]
            for words in usedWords:
                if word == words:
                    hardValue = hardValue+1
                    word = hardWords[hardValue]
                    if hardValue == 9:
                        print("You have already played all of the hard words.", "\nYou have completed the game.")
                        break
            print ("You have chosen " + difficulty + " difficulty.")
            break
        else:
            print("Please enter a valid input.")

#creates function to start playing
def playGame():
    difficulty()
    usedWords.append(word)
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
            print ("\nCongratulations! You won!")
        # exit the script
            break            

        #if user has input guesses, print them out
        if len(guesses) > 0:
            print("\nPrevious guesses: ", *guesses)

        # ask the user go guess a character
        guess = input("guess a character:") 

        # checks to see if the guess has already been guessed
        if guess not in guesses:
            # set the players guess to guesses
            guesses += guess                    

            # if the guess is not found in the secret word
            if guess not in word:  
    
            # turns counter decreases with 1 (now 9)
                turns -= 1        
    
            # print wrong
                print ("\nWrong")  
    
            # how many turns are left
                print ("You have", + turns, 'more guesses' )
    
            # if the turns are equal to zero
                if turns == 0:           
        
                # print "You Lose"
                    print ("You Lose"  )
                    print ("The word was " + word)
        else:
            print("\nYou already guessed that letter.", "\nGuess again.")

#ask the user if they want to play again
def playAgainFunct():
    playAgain = input("Would you like to play again? (y/n) ")
    if playAgain == "y":
        playGame()
    elif playAgain == "n":
        print("Thanks for playing!")
        time.sleep(1)
        exit()
    else:
        print("Please enter a valid input.")
        playAgainFunct()
