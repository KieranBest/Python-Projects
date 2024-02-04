import pyautogui # pip install pyautogui

numberOne = 0
numberTwo = 1
numberThree = 0

while True:
    numberThree = numberOne + numberTwo
    numberOne = numberTwo
    numberTwo = numberThree
    msg = str(numberOne)
    pyautogui.typewrite(msg + '\n', interval=5)
