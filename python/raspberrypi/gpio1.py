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
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
   GPIO.output(14, True) 
   GPIO.output(15, True) 
   GPIO.output(18, True) 
   GPIO.output(23, True) 
   GPIO.output(24, True) 
   time.sleep(50)

   GPIO.output(14, False)
   GPIO.output(15, False)
   GPIO.output(18, False)
   GPIO.output(23, False)
   GPIO.output(24, False)
   time.sleep(.5)

   GPIO.output(14, True)
   GPIO.output(15, False)
   GPIO.output(18, False)
   GPIO.output(23, False)
   GPIO.output(24, False)
   time.sleep(.5)

   GPIO.output(14, False)
   GPIO.output(15, True)
   GPIO.output(18, False)
   GPIO.output(23, False)
   GPIO.output(24, False)
   time.sleep(.5)

   GPIO.output(14, False)
   GPIO.output(15, False)
   GPIO.output(18, True) 
   GPIO.output(23, False)
   GPIO.output(24, False)
   time.sleep(.5)

   GPIO.output(14, False)
   GPIO.output(15, False)
   GPIO.output(18, False)
   GPIO.output(23, True) 
   GPIO.output(24, False)
   time.sleep(.5)

   GPIO.output(14, False)
   GPIO.output(15, False)
   GPIO.output(18, False)
   GPIO.output(23, False)
   GPIO.output(24, True) 
   time.sleep(.5)
   GPIO.cleanup()
