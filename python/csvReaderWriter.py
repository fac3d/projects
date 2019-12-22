#
# Filename: csvReaderWriter.py
#
# Contains functions that write and read a simple csv file.
#
# Date: 01-Dec-19
#
import csv

def myWriter():
   print("-Entry- myWriter")
   
   with open('schedule.csv', 'w', newline='') as csvfile:
      linewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
      linewriter.writerow(['TaskName', 'StartDate','StartTime','Length','Task', \
                         'Comments','PosixStart'])
      
      linewriter.writerow(['000000','','00:30','10','GetTleUrl', \
                         "Get the latest TLE",'1574636961'])
      
      linewriter.writerow(['','13-NOV-19','00:30','10','GetTleUrl', \
                         "Get the latest TLE",'1574636961'])
      
      linewriter.writerow(['000002','13-NOV-19','00:30','10','GetTleUrl', \
                         "",'1574636961'])
      
      linewriter.writerow(['000003','13-NOV-19','00:30','75','GetTleUrl', \
                         "",'1574636961'])
      
      linewriter.writerow(['000004','13-NOV-19','00:30','75','', \
                         "Get the latest TLE",'1574636961'])
      
      linewriter.writerow(['000005','13-NOV-19',' ','60','GetTleUrl', \
                         "Get the latest TLE",'1574636961'])

      linewriter.writerow(['000006','13-NOV-19','00:15','60','GetTleUrl', \
                         "Get the latest TLE",''])
      
      linewriter.writerow(['000006','13-NOV-19','00:15','60','GetTleUrl', \
                         "Get the latest TLE",'1574636961'])   
   
   print("-Exit- myWriter")
  

def myReader():
   print("-Entry- myReader")
   
   n=0
   with open('schedule.csv', newline='') as csvfile:
      linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in linereader:
         print(', '.join(row))
         
   print("-Exit- myReader")

def myRowChecker():
   '''
      myRowChecker looks at the 4th column. Values between 0 and 60
      are fine. Outside of 60 flags length of support not ok error.
   '''
   print("-Entry- myRowChecker")
   n=0
   with open('schedule.csv', newline='') as csvfile:
      linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in linereader:
         for i in range(len(row)):
             e=0
             print(len(row),row)
             
             # check task name
             v=1
             v=len(row[0])
             if(v == 0):
                e=1
                print('-Error- TaskName has 0 length')
                
             # check StartDate
             v=1
             v=len(row[1])
             if(v == 0):
                e=1
                print('-Error- StartDate has 0 length')
                
             # check StartTime  
             v=1
             v=len(row[2])
             if(v == 0):
                e=1
                print('-Error- StartTime has 0 length')
                
             # test length of support  
             try:
                n=int(row[3]) 
                if((n<0) or (n>60)):
                   e=1
                   print('-Error- Length of support incorrect')
             except:
                print('int n exception')
                
             # check Task  
             v=1
             v=len(row[4])
             if(v < 1):
                e=1
                print('-Error- Task has 0 length')
                
             # check Comments   
             v=1
             v=len(row[5])
             if(v < 1):
                e=1
                print('-Error- Comments has 0 length')
               
             # Check PosixStart   
             v=1
             v=len(row[6])
             if(v < 1):
                e=1
                print('-Error- PosixStart has 0 length')

             if(e == 0):
                print('Good line is:',row);
                
             break
              
   print("-Exit- myRowChecker")


def testRowFunction():
   print("-Enter- testRowFunction")
   
   with open('schedule.csv', newline='') as csvfile:
      linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for item in linereader:
         x=0
         while(x < len(item)):
            if(item[x].isdigit()):
               print(item[x], 'is a digit')
               if(int(item[x]) > 5):
                  print('item['+str(int(x))+'] > 5')
                  print('multiply is: '+item[x]+'*4=' + str(int(item[x])*4))
            elif(item[x].isdecimal()):
               print(item[x], 'is decimal')
            elif(item[x].isalpha()):
               print(item[x], 'is alphanumeric')
            elif(item[x].isnumeric()):
               print(item[x], 'is numeric')
            elif(item[x].isspace()):
               print(item[x], 'is space')
            else:
               print(item[x], 'is unknown')
            x+=1


         
   print("-Exit- testRowFunction")


def multiplyTable():
   print('-Entry- multiplyTable')
   print('    ----------------------------------------')
   print("   |  {}|  {}|  {}|  {}|  {}|  {}|  {}|  {}|  {}| {}|"\
         .format("1","2","3","4","5","6","7","8","9","10"))
   print('    ----------------------------------------')
   for x in range(1,11,1):
      print('{:3d}'.format(x),end='|')
      for y in range(1,12,1):
         z=x*y
         if (y == 11):
            print(' ')
            print('    ----------------------------------------')

         else:
            #print(str(z).format('right aligned'), end='|')
            print('{:3d}'.format(z),end='|')
            #print('%02d' % z)
            
   print('-Exit- multiplyTable')

#with open('schedule.csv', newline='') as csvfile:
#    linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in linereader:
#        print(', '.join(row))
#         outString='INSERT INTO testcsv(names,classes, mark) \
#                   VALUES("%s", "%s", "%s")'
#         print(outString)
