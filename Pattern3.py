import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]


#Reset function PROTOTYPE
def reset(x):
        for i in range(0,15):
            GPIO.output(GRID[i],False)
def resetlayer(x):
    for i in range(0,4):
        GPIO.output(LAYER[i],False)

        
def base1():
    GPIO.output(32,True)
    GPIO.output(35,True)
    GPIO.output(11,True)
    GPIO.output(19,True)
    GPIO.output(21,True)
    time.sleep(1)
    GPIO.output(35,False)
    GPIO.output(11,False)
    GPIO.output(19,False)
    GPIO.output(21,False)
    GPIO.output(32,False)
    time.sleep(1)

def sqr1():
    GPIO.output(36,True)
    GPIO.output(12,True)
    GPIO.output(33,True)
    GPIO.output(29,True)
    GPIO.output(15,True)
    time.sleep(1)
    GPIO.output(12,False)
    GPIO.output(33,False)
    GPIO.output(29,False)
    GPIO.output(15,False)
    GPIO.output(36,False)
    time.sleep(1)

def sqr2():
    GPIO.output(38,True)
    GPIO.output(12,True)
    GPIO.output(33,True)
    GPIO.output(29,True)
    GPIO.output(15,True)
    time.sleep(1)
    GPIO.output(12,False)
    GPIO.output(33,False)
    GPIO.output(29,False)
    GPIO.output(15,False)
    GPIO.output(38,False)
    time.sleep(1)

def base2():
    GPIO.output(40,True)
    GPIO.output(35,True)
    GPIO.output(11,True)
    GPIO.output(19,True)
    GPIO.output(21,True)
    time.sleep(1)
    GPIO.output(35,False)
    GPIO.output(11,False)
    GPIO.output(19,False)
    GPIO.output(21,False)
    GPIO.output(40,False)
    time.sleep(1)

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


case = { 1 : base1,
         2 : sqr1,
         3 : sqr2,
         4 : base2,
         }

try:
    while(True):
        reset(GRID)
        resetlayer(LAYER)
        for i in range(1,5):
            case[i]()
            print('i=' + str(i))

except KeyboardInterrupt:
    GPIO.cleanup()
