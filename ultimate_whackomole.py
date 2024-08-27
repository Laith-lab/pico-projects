from machine import Pin, PWM, UART
from utime import sleep
import random
import sys

LEDRED = Pin(14, Pin.OUT)
LEDYELLOW = Pin(13, Pin.OUT)
LEDGREEN = Pin(15, Pin.OUT)
BUTTONONE = Pin(10, Pin.IN, Pin.PULL_DOWN)
BUTTONTWO = Pin(9, Pin.IN, Pin.PULL_DOWN)
BUTTONTHREE = Pin(7, Pin.IN, Pin.PULL_DOWN)
points = 0


# bongbong_buttons = [LEDRED, LEDYELLOW, LEDGREEN]

bongbong_buttons = {
        LEDGREEN: BUTTONONE,
        LEDYELLOW: BUTTONTWO,
        LEDRED: BUTTONTHREE
}

def setDifficulty(waitTime, startTime, endTime):
    bongbongchoice.value(1)
    sleep(waitTime)
    bongbongchoice.value(0)
    sleep(1)
    sleep(random.randrange(startTime, endTime))




    

while BUTTONONE.value() ==  0:
    LEDRED.value(0)
    LEDGREEN.value(1)
    sleep(0.5)
    LEDGREEN.value(0)
    LEDYELLOW.value(1)
    sleep(0.5)
    LEDYELLOW.value(0)
    LEDRED.value(1)
    sleep(0.5)
    start = True

   
difficulty = int(input("enter difficulty: "))

easyDifficulty = setdifficulty(2,1,10)
mediumDifficulty = setDifficulty(2,1,5)
hardDifficulty = setDifficulty(2,1,2)

while start:
    LEDRED.value(0)
    LEDGREEN.value(0)
    LEDYELLOW.value(0)

    match(difficulty):
        case 1:
            easyDifficulty
        case 2:
            mediumDifficulty
        case 3:
            hardDifficulty
        case _:
            print("huh")


   
    # check for mechanical bouncing   
    bongbongchoice = random.choice(list(bongbong_buttons.keys()))

    # bongbongchoice = random.choice(bongbong_buttons)


    correct_button = bongbong_buttons[bongbongchoice]
    print(f"Lit LED: {bongbongchoice}")
    print(f"Button associated with the lit LED: {correct_button}")
    print(f"Button state: {correct_button.value()}")
    if correct_button.value() == 1:
        print("you did it !!")
    else:
        print("you suck.")
        # if the button that the user has pressed is the corresponding value to the correct key, then the user gets a point.
        # If the user has pressed the button at the same time that the LED is on, then the user gets a point. HOw to incorperate both of those conditions in one? I have no idea.

