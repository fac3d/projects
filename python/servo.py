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

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm18.ChangeDutyCycle(duty)
        pwm19.ChangeDutyCycle(duty)
	print ("duty is: angle is:", duty, angle)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()



