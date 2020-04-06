#!/usr/bin/env python
# encoding: utf-8
 
import RPi.GPIO
import time
import json
import threading
 
class rgbThread(threading.Thread):
    def __init__(self, r, g, b):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.isRun = True
        print('init rgb')
        f = open("./config.json", "r", encoding="UTF-8")
        config_dict = json.load(f)
        R = config_dict['rgb-r-pin']
        G = config_dict['rgb-g-pin']
        B = config_dict['rgb-b-pin']

        print('RGB-PIN',R,G,B)

        RPi.GPIO.setmode(RPi.GPIO.BCM)

        RPi.GPIO.setup(R, RPi.GPIO.OUT)
        RPi.GPIO.setup(G, RPi.GPIO.OUT)
        RPi.GPIO.setup(B, RPi.GPIO.OUT)

        self.pwmR = RPi.GPIO.PWM(R, 70)
        self.pwmG = RPi.GPIO.PWM(G, 70)
        self.pwmB = RPi.GPIO.PWM(B, 70)

        self.pwmR.start(0)
        self.pwmG.start(0)
        self.pwmB.start(0)

    def stop(self):
        self.isRun = False
        print('rgbThread stopped',self.isRun)
        self.pwmR.stop()
        self.pwmG.stop()
        self.pwmB.stop()
        #RPi.GPIO.cleanup()

    def run(self):
        print('rgbThread run=', self.r,self.g,self.b)
        while self.isRun:
            try:
                self.pwmR.ChangeDutyCycle(self.r)
                self.pwmG.ChangeDutyCycle(self.g)
                self.pwmB.ChangeDutyCycle(self.b)
            except:
                self.pwmR.stop()
                self.pwmG.stop()
                self.pwmB.stop()
                #RPi.GPIO.cleanup()
    
    

