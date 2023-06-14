userInput = input("Enter a string: ")
stringLength = userInput.__len__()
for x in range(0,stringLength,2):
    value1 = userInput[x]
    if(x+1 < stringLength):
        value2 = userInput[x+1]
        userInput = userInput[:x] + value2 + value1 + userInput[x+2:]
        # kept getting an error when I tried to do userInput[x] = value2 so used this method instead
print(userInput)

# https://realpython.com/python-strings/#:~:text=String%20Indexing,-Often%20in%20programming&text=Individual%20characters%20in%20a%20string,index%201%20%2C%20and%20so%20on.
# Modifying Strings
