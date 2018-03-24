#!/usr/bin/python


from Tkinter import *
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

def gpio14():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.IN)
        if GPIO.input(14) == True:
		GPIO.setup(14, GPIO.OUT)
		GPIO.output(14, False)
	else:
		GPIO.setup(14, GPIO.OUT)
		GPIO.output(14, True)

def gpio15():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, True)

def gpio18():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, True)

def gpio23():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, True)

def gpio24():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(24, GPIO.OUT)
	GPIO.output(24, True)

def gpio25():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, True)

def gpio8():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, True)

def gpio7():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7, True)

def gpio12():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, True)

def gpio16():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, True)

def gpio20():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, True)

def gpio21():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, True)

def gpio26():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, True)

def gpio19():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(19, GPIO.OUT)
	GPIO.output(19, True)

def gpio13():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, True)

def gpio6():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.OUT)
	GPIO.output(6, True)

def gpio5():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(5, GPIO.OUT)
	GPIO.output(5, True)

def gpio11():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, True)

def gpio9():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(9, GPIO.OUT)
	GPIO.output(9, True)

def gpio10():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(10, GPIO.OUT)
	GPIO.output(10, True)

def gpio22():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(22, True)

def gpio27():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(27, GPIO.OUT)
	GPIO.output(27, True)

def gpio17():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, True)

def gpio4():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)
	GPIO.output(4, True)

def gpio3():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(3, GPIO.OUT)
	GPIO.output(3, True)

def gpio2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.OUT)
	GPIO.output(2, True)
	GPIO.output(2, False)

def off():
	GPIO.cleanup()                 

def quit():
	sys.exit()                     

root = Tk()
Button(None, text="GPIO14", command=gpio14).pack(side=LEFT)
Button(None, text="GPIO15", command=gpio15).pack(side=LEFT)
Button(None, text="GPIO18", command=gpio18).pack(side=LEFT)
Button(None, text="GPIO23", command=gpio23).pack(side=LEFT)
Button(None, text="GPIO24", command=gpio24).pack(side=LEFT)
Button(None, text="GPIO25", command=gpio25).pack(side=LEFT)
Button(None, text="GPIO8", command=gpio8).pack(side=LEFT)
Button(None, text="GPIO7", command=gpio7).pack(side=LEFT)
Button(None, text="GPIO12", command=gpio12).pack(side=LEFT)
Button(None, text="GPIO16", command=gpio16).pack(side=LEFT)
Button(None, text="GPIO20", command=gpio20).pack(side=LEFT)
Button(None, text="GPIO21", command=gpio21).pack(side=LEFT)
#
Button(None, text="GPIO2", command=gpio2).pack(side=LEFT)
Button(None, text="OFF",    command=off).pack(side=RIGHT)
Button(None, text="QUIT",   command=quit).pack(side=RIGHT)


root.mainloop()



