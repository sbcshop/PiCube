#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


#Global variable
GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]
VGRID = [37,33,29,22,35,31,23,21,11,13,16,19,7,12,15,18]

#Reset function PROTOTYPE
def reset(x):
        for i in range(0,15):
                GPIO.output(GRID[i],False)
def resetlayer(x):
        for i in range(0,4):
                GPIO.output(LAYER[i],False)

        
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


#Patterns
try:
    while(True):
        reset(GRID)
        resetlayer(LAYER)


#Horizontal Curtain  
        GPIO.output(32,True)
        GPIO.output(36,True)
        GPIO.output(38,True)
        GPIO.output(40,True)
        for k in range(0,16):
                print 'LED' + str(k+1) + '\tON'
                GPIO.output(GRID[k],True)
                time.sleep(0.04)

        for l in range(0,16):
                print 'LED'+ str(l+1) + '\tOFF'
                GPIO.output(GRID[l],False)
                time.sleep(0.04)
        GPIO.output(32,False)
        GPIO.output(36,False)
        GPIO.output(38,False)
        GPIO.output(40,False)

                
#Horizontal Pattern
        for a in range(0,4):
                print '\nlayer number ' +str(a+1)
                GPIO.output(LAYER[a],True)
                
                for i in range(0,16):
                        print 'LED ' + str(i+1) + '\tON' 
                        GPIO.output(GRID[i],True)
                        time.sleep(0.04)
                for j in range(0,16):
                        print 'LED' + str(j+1) + '\tOFF'
                        GPIO.output(GRID[j], False)
                        time.sleep(0.04)
                GPIO.output(LAYER[a],False)
                print 'layer number ' +str(a+1) +'\tOFF'
                
#Vertical Pattern
        for n in range(0,16):
                print 'n=' + str(n) 
                GPIO.output(GRID[n],True)
                time.sleep(0.04)
        
                for m in range(0,4):
                        print 'm=' + str(m)
                        GPIO.output(LAYER[m],True)
                        time.sleep(0.04)
                for o in range(0,4):
                        print'o=' + str(o)
                        GPIO.output(LAYER[o],False)
                        time.sleep(0.04)
                GPIO.output(GRID[n],False)
                print 'n=' +str(n) + '\tOFF'
                time.sleep(0.04)
    
#Vertical Curtain  
        GPIO.output(32,True)
        GPIO.output(36,True)
        GPIO.output(38,True)
        GPIO.output(40,True)
        for k in range(0,16):
                print 'VERTICAL LED ' + str(i+1) + '\tON'
                GPIO.output(VGRID[k],True)
                time.sleep(0.04)

        for l in range(0,16):
                print 'VERTICAL LED '+ str(i+1) + '\tOFF'
                GPIO.output(VGRID[l],False)
                time.sleep(0.04)
                
except KeyboardInterrupt:
    GPIO.cleanup()
