#!/usr/bin/env python
# encoding: utf-8
 
import RPi.GPIO
import time
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
f = open("./config.json", "r", encoding="UTF-8")
config_dict = json.load(f)
R = config_dict['rgb-r-pin']
G = config_dict['rgb-g-pin']
B = config_dict['rgb-b-pin']

print('RGB',R,G,B)
 
RPi.GPIO.setmode(RPi.GPIO.BCM)
 
RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)
 
pwmR = RPi.GPIO.PWM(R, 70)
pwmG = RPi.GPIO.PWM(G, 70)
pwmB = RPi.GPIO.PWM(B, 70)
 
pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

def rgb(r=0, g=100, b=100):
    try:
        pwmR.ChangeDutyCycle(r)
        pwmG.ChangeDutyCycle(g)
        pwmB.ChangeDutyCycle(b)
    
    except:
        pwmR.stop()
        pwmG.stop()
        pwmB.stop()
        RPi.GPIO.cleanup()
 

