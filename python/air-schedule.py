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
    conn.execute('''CREATE TABLE SCHEDULE(ID INT PRIMARY KEY NOT NULL, \
                    FLTNUM TEXT, DEPART_CITY TEXT, ARRIVE_CITY TEXT, 
                    DEPART_TIME TEXT, ARRIVE_TIME TEXT, DURATION INT);''')
    conn.close()

def insertdb():
    conn=sqlite3.connect('air-schedule.db')
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, \
                  DEPART_TIME, ARRIVE_TIME, DURATION) VALUES(1, '741', 'HNL', 'LIH', '23-MAR-18 0640', '23-MAR-18 0740', 35)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, \
                  DEPART_TIME, ARRIVE_TIME, DURATION) VALUES(2, '742', 'LIH', 'HNL', '23-MAR-18 0640', '23-MAR-18 0740', 35)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, \
                  DEPART_TIME, ARRIVE_TIME, DURATION) VALUES(3, '743', 'HNL', 'OGG', '23-MAR-18 0740', '23-MAR-18 0840', 30)");
    conn.execute("INSERT INTO SCHEDULE(ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, \
                  DEPART_TIME, ARRIVE_TIME, DURATION) VALUES(4, '744', 'OGG', 'HNL', '23-MAR-18 0740', '23-MAR-18 0840', 30)");
    conn.commit()
    conn.close()

def readdb():
    conn=sqlite3.connect('air-schedule.db')
    cursor=conn.execute("SELECT ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, DEPART_TIME, ARRIVE_TIME, DURATION FROM SCHEDULE")

    for row in cursor:
        print ("ID=", row[0])
        print ("FLTNUM=", row[1])   
        print ("DEPART_CITY=", row[2])   
        print ("ARRIVE_CITY=", row[3])
        print ("DEPART_TIME=", row[4])   
        print ("ARRIVE_TIME=", row[5])
        print ("DURATION=", row[6])   

    cursor=conn.execute("SELECT ID, FLTNUM, DEPART_CITY, ARRIVE_CITY, DEPART_TIME, ARRIVE_TIME, DURATION FROM SCHEDULE")
    for row in cursor:
       print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

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


