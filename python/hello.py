import time
from time import gmtime, strftime
import mysql.connector
from mysql.connector import Error

print ("Hello")
#timeString=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#print(timeString=strftime("%d-%b-%Y %H:%M:%S", gmtime())


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='frank',
                                         user='root',
                                         password='root')
    sql_select_Query = "select * from test5"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0],)

    mySql_insert_query = """INSERT INTO test5 (a5) 
                           VALUES 
                           ("33") """
    result = cursor.execute(mySql_insert_query)
    connection.commit()
    print("Record inserted successfully into test5 table")
          
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


