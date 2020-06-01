# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:50:43 2020

@author: Alain Honore Kubwayo
"""

import time
import RPi.GPIO as GPIO

GPIO_BUZZER = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_BUZZER,GPIO.OUT)

try: 
    while True:
        GPIO.output(4,0)
        time.sleep(.2)
        GPIO.output(4,1)
        time.sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit
              
        
        



