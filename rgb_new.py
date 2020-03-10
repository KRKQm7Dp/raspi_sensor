#!/usr/bin/env python
# encoding: utf-8
 
import RPi.GPIO
import time
import json
 
class rgbThread(threading.Thread):
    def __init__(self, r, g, b):
        super().__init__(self)
        self.r = r
        self.g = g
        self.b = b
        self.isRun = True
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
        self.pwmR.stop()
        self.pwmG.stop()
        self.pwmB.stop()
        self.RPi.GPIO.cleanup()

    def rgb(self, r=0, g=100, b=100):
        

    def run(self):
        print('rgb=', r,g,b)
        while True:
            try:
                self.pwmR.ChangeDutyCycle(self.r)
                self.pwmG.ChangeDutyCycle(self.g)
                self.pwmB.ChangeDutyCycle(self.b)
            except:
                self.pwmR.stop()
                self.pwmG.stop()
                self.pwmB.stop()
                self.RPi.GPIO.cleanup()
    
    

