from threading import Thread
from copy import deepcopy
from time import sleep
from time import time
import RPi.GPIO as GPIO
import random
import math


class Cube(object):
    """docstring for Cube
        mode 0 for continuous running
        mode 1 for callback with time difference
        this driver assumes that each column has its own GPIO and each layer has again its own GPIO
    """

    def __init__(self, leds, mode):
        super(Cube, self).__init__()
        self.leds = leds
        self._renderer = CubeRender(mode)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for x in leds["bottom"]:
            for y in x:
                GPIO.setup(y, GPIO.OUT)
                GPIO.output(y, False)
        for z in leds["layers"]:
            GPIO.setup(z, GPIO.OUT)
            GPIO.output(z, False)
        self._renderer.nextFrame = list(list(list()))
        self._renderer.leds = leds
        self._renderer.start();

    def set_callback(self, func):
        pass
        
    def set_cube(self, image):
        self._renderer.nextFrame = image[:]

class CubeRender(Thread):
    """docstring for CubeRender"""
    def __init__(self, mode):
        super(CubeRender, self).__init__()
        self.mode = mode
        self.on = True

    def run(self):
        if self.mode == 0:
            while(self.on):
                self.frame = self.nextFrame[:]
                for z, zval in enumerate(self.frame):
                    for y, yval in enumerate(zval):
                        for x, xval in enumerate(yval):
                            GPIO.output(self.leds["bottom"][x][y], xval)
                    GPIO.output(self.leds["layers"][z], True)
                    GPIO.output(self.leds["layers"][z], False)
        else:
            bitangle = [1,2,4,8]
            while(self.on):
                self.frame = deepcopy(self.nextFrame)
                for angle in bitangle:
                    for i in range(0, angle):
                        for z, zval in enumerate(self.frame):
                            for y, yval in enumerate(zval):
                                for x, xval in enumerate(yval):
                                    GPIO.output(self.leds["bottom"][x][y], xval % 2 == 1)
                                    if (i + 1 == angle):
                                        self.frame[z][y][x] = self.frame[z][y][x] >> 1
                            GPIO.output(self.leds["layers"][z], True)
                            GPIO.output(self.leds["layers"][z], False)

class drop(object):
    """docstring for drop"""
    def __init__(self, x, y, speed):
        super(drop, self).__init__()
        self.x = x
        self.y = y
        self.z = 3
        self.speed = speed
        self.current_jump = 0

    def inc(self):
        if (self.current_jump + 1 > self.speed):
            self.current_jump = 0
            self.z = self.z - 1
        else:
            self.current_jump = self.current_jump + 1

class point(object):
    """docstring for point"""
    def __init__(self):
        super(point, self).__init__()
        self.x = random.randint(0,3)
        self.y = random.randint(0,3)
        self.z = random.randint(0,3)

    def attempt(self, coord, direction):
        if direction != 0:
            coord = coord + direction
            if coord > 3 or coord < 0:
                coord = coord - direction
        return coord

    def move(self):
        self.x = self.attempt(self.x, random.randint(-1,1))
        self.y = self.attempt(self.y, random.randint(-1,1))
        self.z = self.attempt(self.z, random.randint(-1,1))
        

class animateCube(object):
    """docstring for animateCube"""
    def __init__(self, controller):
        super(animateCube, self).__init__()
        self.controller = controller
        random.seed(time())
        self.alive = True

    def wave(self, delay = 0.1, timeout=120):
        i = 0
        t = time()
        while (self.alive and time() - t <= timeout):
            sleep(delay)
            l = list()
            for z in range(0,4):
                l.insert(z, list())
                for y in range(0,4):
                    l[z].insert(y, list())
                    for x in range(0,4):
                        l[z][y].insert(x, False)
            for z in range(0,4):
                for y in range(0,4):
                    for x in range(0,4):
                        l[round(3 * math.sin((i + x + i * y * 0.1) * 0.3) ** 2)][y][x] = True
            i = i + 1
            self.controller.set_cube(l)
    
    def rain(self, timeout=120):
        drops = list()
        t = time()
        while (self.alive and time() - t  <= timeout):
            sleep(0.04)
            l = list()
            for z in range(0,4):
                l.insert(z, list())
                for y in range(0,4):
                    l[z].insert(y, list())
                    for x in range(0,4):
                        l[z][y].insert(x, False)
            if (random.randint(0,10) > 7):
                x = drop(random.randint(0,3),random.randint(0,3), random.randint(0,6))
                drops.append(x)
            for i, obj in enumerate(drops):
                l[obj.z][obj.y][obj.x] = True
                obj.inc()
                if obj.z < 0:
                    drops.pop(i)
            self.controller.set_cube(l)

    def points(self, count = 2, timeout=120):
        points = list()
        for x in range(0, count):
            points.append(point())
        t = time()
        while (self.alive and time() - t <= timeout):
            sleep(0.05)
            l = list()
            for z in range(0, 4):
                l.insert(z, list())
                for y in range(0, 4):
                    l[z].insert(y, list())
                    for x in range(0, 4):
                        l[z][y].insert(x, False)
            for obj in points:
                obj.move()
                l[obj.z][obj.y][obj.x] = True
            self.controller.set_cube(l)

    def fade_verify(self, l):
        current = l[0][0][0]
        for z in range(0,4):
            for y in range(0,4):
                for x in range(0,4):
                    if current != l[z][y][x]:
                        return False
        return True

    def fade(self, timeout=120):
        l = list()
        for z in range(0, 4):
            l.insert(z, list())
            for y in range(0, 4):
                l[z].insert(y, list())
                for x in range(0, 4):
                    l[z][y].insert(x, False)
        flip = True
        t = time()
        while (self.alive and time() - t <= timeout):
            sleep(0.01)
            l[random.randint(0, 3)][random.randint(0, 3)][random.randint(0, 3)] = flip
            if self.fade_verify(l):
                flip = not flip
            self.controller.set_cube(l)

    def swirl(self, timeout=120):
        columns = [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3), (0,2), (0,1), (1,1), (2,1), (2,2), (1,2)]
        t = time()
        while (self.alive and time() - t <= timeout):
            for i in range(0,3):
                l = list()
                for z in range(0,4):
                    l.insert(z, list())
                    for y in range(0,4):
                        l[z].insert(y, list())
                        for x in range(0,4):
                            l[z][y].insert(x, False)
                for col in range(0,16):
                    for led in range(0,4):
                        if i == 0:
                            l[columns[col][0]][columns[col][1]][led] = True
                        elif i == 1:
                            l[columns[col][0]][led][columns[col][1]] = True
                        elif i == 2:
                            l[led][columns[col][0]][columns[col][1]] = True
                    self.controller.set_cube(l)
                    sleep(0.2)

    def lines(self):
        pass

if __name__ == "__main__":
    leds = {
        "bottom":[[7,11,35,37],[12,13,31,33],[15,16,23,29],[18,19,21,22]],
        "layers":[40,38,36,32]
    }
    controller = Cube(leds, 0)
    animations = animateCube(controller)
    while True:
            animations.wave()
            animations.rain()
            animations.points()
            animations.fade()
            animations.swirl()
