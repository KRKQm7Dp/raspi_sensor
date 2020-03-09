#!/usr/bin/env python
# encoding: utf-8
 
import RPi.GPIO
import time
 
R,G,B=13,19,26
 
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
 
try:
 
    t = 0.4
    while True:
        # 红色灯全亮，蓝灯，绿灯全暗（红色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
 
except KeyboardInterrupt:
    pass
 
pwmR.stop()
pwmG.stop()
pwmB.stop()
 
RPi.GPIO.cleanup()
