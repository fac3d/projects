from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

#
# the first number is the GPIO channel.
# the second number is the frequency or rate.
# 100 is 100 times per second.
#
pwm18 = GPIO.PWM(18, 60)
pwm19 = GPIO.PWM(19, 60)

#
#
#
pwm18.start(5)
pwm19.start(5)

angle = 10
duty = float(angle) / 10.0 + 2.5
pwm18.ChangeDutyCycle(duty)
pwm19.ChangeDutyCycle(duty)
print ("duty is: angle is:", duty, angle)
time.sleep(5)

angle = 30
duty = float(angle) / 10.0 + 2.5
pwm18.ChangeDutyCycle(duty)
pwm19.ChangeDutyCycle(duty)
print ("duty is: angle is:", duty, angle)
time.sleep(5)

angle = 50
duty = float(angle) / 10.0 + 2.5
pwm18.ChangeDutyCycle(duty)
pwm19.ChangeDutyCycle(duty)
print ("duty is: angle is:", duty, angle)
time.sleep(5)

angle = 0
duty = float(angle) / 10.0 + 2.5
pwm18.ChangeDutyCycle(duty)
pwm19.ChangeDutyCycle(duty)
print ("duty is: angle is:", duty, angle)
time.sleep (5)




