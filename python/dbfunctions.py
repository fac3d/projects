import time
from time import gmtime, strftime
import mysql.connector
from mysql.connector import Error


def opendb():
    print('opendb:')
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='frank',
                                         user='root',
                                         password='root')
    except Error as e:
        print("Error opening MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")    
    return connection


def closedb(connection):
    e=''
    try:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    except Error as e:
        print("Error closing MySQL", e)
    finally:    
        print("Error closing MySQL", e)

    return 0

def readdb(connection):
    sql_select_Query = "select * from test5"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0],)
    return 0

def writedb():

    return 0


def main():
    connection=opendb()
    closedb(connection)
    opendb(connection)
    readdb(connection)
    writedb(connection)
    closedb(connection)

if __name__ == "__main__":
    main()

    
