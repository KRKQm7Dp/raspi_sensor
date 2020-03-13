#!/usr/bin/python
import RPi.GPIO as GPIO
import json

def switch(flag):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    f = open("./config.json", "r", encoding="UTF-8")
    config_dict = json.load(f)
    pin = config_dict['relay-pin']

    print("relayPin=" , pin)
    if (flag):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
