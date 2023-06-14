nthTerm = 100

numberOne = 0
numberTwo = 1
numberThree = 0

for x in range(nthTerm):
    print(numberOne)
    numberThree = numberOne + numberTwo
    numberOne = numberTwo
    numberTwo = numberThree
