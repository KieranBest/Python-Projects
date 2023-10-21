#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

clock = Tk()

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        display_alarm=Label(clock, text= "The Set Date is:"+date, fg="black",font="Arial").place(x=120,y=150)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)



clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=100,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 150,)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=40, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "white",width = 5).place(x=150,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 5).place(x=190,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 5).place(x=230,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =150,y=70)

clock.mainloop()
#Execution of the window.