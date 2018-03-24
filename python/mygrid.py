#!/usr/bin/python

from Tkinter import *
import os


# Setup the array.
header = ["SATELLITE", "LINK", "START", "LENGTH"]

rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        #e.insert(END, '%d.%d' % (i, j))
        if((i==0) and (j==0)):
            e.insert(END, '%s' % (header[0]))
        if((i==0) and (j==1)):
            e.insert(END, '%s' % (header[1]))
        if((i==0) and (j==2)):
            e.insert(END, '%s' % (header[2]))
        if((i==0) and (j==3)):
            e.insert(END, '%s' % (header[3]))

        cols.append(e)
    rows.append(cols)


def onPress():
    for row in rows:
        for col in row:
            print col.get(),
        print

def quit():
    os._exit(0)

def hqaAdd():
    print "hqaAdd"
    for row in rows:
        #for col in row:
        #    print col.get(), 
        print

def hqaDelete():
    print "hqaDelete"  

def hqaSchedule():
    print "hqaSchedule"


#Button(text='Add', command=hqaAdd).grid(row=0, column=5)
Button(text='Add', command=hqaAdd).grid(row=1, column=5)
Button(text='Add', command=onPress).grid(row=2, column=5)
Button(text='Add', command=onPress).grid(row=3, column=5)
Button(text='Add', command=onPress).grid(row=4, column=5)

#Button(text='Delete', command=onPress).grid(row=0, column=6)
Button(text='Delete', command=onPress).grid(row=1, column=6)
Button(text='Delete', command=onPress).grid(row=2, column=6)
Button(text='Delete', command=onPress).grid(row=3, column=6)
Button(text='Delete', command=onPress).grid(row=4, column=6)

#Button(text='Delete', command=onPress).grid(row=0, column=7)
Button(text='Schedule', command=onPress).grid(row=1, column=7)
Button(text='Schedule', command=onPress).grid(row=2, column=7)
Button(text='Schedule', command=onPress).grid(row=3, column=7)
Button(text='Schedule', command=onPress).grid(row=4, column=7)

Button(text='Quit', command=quit).grid(row=5, column=0)

mainloop()



