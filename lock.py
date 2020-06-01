# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:50:43 2020

@author: Alain Honore Kubwayo
"""

import time
import RPi.GPIO as GPIO

# Setting pin 23 as output
GPIO_RELAY = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_RELAY, GPIO.OUT)
GPIO.output(GPIO_RELAY, GPIO.LOW)

# Face Recognized?
GPIO.output(GPIO_RELAY, GPIO.HIGH)
print("Door Unlocked")
time.sleep(10) # Door Remains Unlcoked for 10 seconds
GPIO.output(GPIO_RELAY, GPIO.LOW)

# Face Unrecognized?
print("Unidentified => Unauthorized!")
GPIO.output(GPIO_RELAY, GPIO.LOW)

GPIO.cleanup()

