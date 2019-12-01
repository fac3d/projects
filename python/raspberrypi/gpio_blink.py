#!/usr/bin/python

# gpio_blink.py
# by Scott Kildall (www.kildall.com)
# LED is on pin 4, use a 270 Ohm resistor to ground
# run as sudo gpio_blink.py
# http://www.instructables.com/id/Raspberry-Pi-Python-scripting-the-GPIO/step6/Blink-an-LED-in-Python/

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
   GPIO.output(24,True)
   GPIO.output(23,False)
   time.sleep(1)
   GPIO.output(24,False)
   GPIO.output(23,True)
   time.sleep(1)



