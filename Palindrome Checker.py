userInput = input("Enter a string: ")
reversedUserInput = userInput[::-1]

print(userInput)
print(reversedUserInput)

if userInput == reversedUserInput:
    print(True)
else:
    print(False)
