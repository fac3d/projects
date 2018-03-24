#!/usr/bin/python

from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    pitch, roll, yaw = sense.get_orientation().values()
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    pitch=round(pitch, 2)
    roll=round(roll, 2)
    yaw=round(yaw, 2)

    print("pitch=%s, roll=%s, yaw=%s t=%s, p=%s, h=%s" % (pitch, yaw, roll, t, p, h))
    time.sleep(0.5)

