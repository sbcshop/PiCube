#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


#Global variable
GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]


#Reset function PROTOTYPE
def reset(x):
     for i in range(0,15):
        GPIO.output(GRID[i],False)
def resetlayer(x):
    for i in range(0,4):
        GPIO.output(LAYER[i],False)

#Pattern prototypes
def smiley():
    GPIO.output(40, True)
    GPIO.output(38, True)
    GPIO.output(36, True)
    GPIO.output(32, True)
    GPIO.output(11, True)
    GPIO.output(35, True)
    GPIO.output(15, True)
    GPIO.output(19, True)
    GPIO.output(21, True)
    GPIO.output(29, True)
    time.sleep(0.5)
    GPIO.output(40, False)
    GPIO.output(38, False)
    GPIO.output(36, False)
    GPIO.output(32, False)
    GPIO.output(11, False)
    GPIO.output(35, False)
    GPIO.output(15, False)
    GPIO.output(19, False)
    GPIO.output(21, False)
    GPIO.output(29, False)
    time.sleep(0.5)

# Layers
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

# Individual LED
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#Pattern

try:
    while(True):
        reset(GRID)
        resetlayer(LAYER)
        smiley()
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
