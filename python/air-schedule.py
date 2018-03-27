#!/usr/bin/python3
#
# Filename: air-schedule.py
#
# Purpose: python and sqlite example.
#
# Date: 26-Mar-2018
#
#######################################################################
import sqlite3

# Functions
def opendb():
    conn=sqlite3.connect('air-schedule.db')
    conn.execute('''CREATE TABLE SCHEDULE(ID INT PRIMARY KEY NOT NULL, FLTNUM TEXT, DEPART TEXT, ARRIVE TEXT, DURATION INT);''')
    conn.close()

def insertdb():
    conn=sqlite3.connect('air-schedule.db')
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART, ARRIVE, DURATION) VALUES(1, '741', 'HNL', 'LIH', 35)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART, ARRIVE, DURATION) VALUES(2, '742', 'LIH', 'HNL', 35)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART, ARRIVE, DURATION) VALUES(3, '743', 'HNL', 'OGG', 30)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART, ARRIVE, DURATION) VALUES(4, '744', 'OGG', 'HNL', 30)");
    conn.commit()
    conn.close()

def readdb():
    conn=sqlite3.connect('air-schedule.db')
    cursor=conn.execute("SELECT ID, FLTNUM, DEPART, ARRIVE, DURATION FROM SCHEDULE")

    for row in cursor:
        print ("ID=", row[0])
        print ("FLTNUM=", row[1])   
        print ("DEPART=", row[2])   
        print ("ARRIVE=", row[3])
        print ("DURATION=", row[4])   

    conn.close()
#
# main
#

try:
    opendb()
except sqlite3.OperationalError:
    print("Exception: OpenDbFailed")
else:
    print()

try:
    insertdb()
except sqlite3.OperationalError:
    print("Exception: InsertDbFailed")
except sqlite3.IntegrityError:
    print("Exception: InsertDbFailed")
else:
    print()

try:
    readdb()
except sqlite3.OperationalError:
    print("Exception: ReadDbFailed")
else:
    print()

exit


