# open the output file as an input file with readonly access and print all the lines
filename = "C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\movies4.csv" #txt
finput = open( filename , "r" ) # r w a
for line in finput : 
    print (line)
finput.close()

## append a new record at the end
finput = open(filename, "a" ) 
finput.write("Nigel,London,actor\n")
finput.close()


filename = "C:\\Users\\u\\.spyder-py3\\stu_andrea\\returns.csv"
# open the output file as an input file with readonly access and print all the lines
finput = open(filename, "r" ) 
count = 0
for line in finput : 
    if count == 0:
        mylist = line.split(',')
        print (mylist[1],mylist[4])
    count += 1
finput.close()

#
filenameBackup = "C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\movies4.csv"
fout = open( filenameBackup, "w" ) # creates the moviesBackup file
data  = "flowers\n"
fout.write(data)
fout.close()
#check backup file
finput = open(filenameBackup, "r" ) 
for line in finput : 
    print (line)
finput.close()

####################################################
"""
per customer what is the average time elapsed between rental date and return date
List the customers who have an avearge of more than 14 days
"""
from datetime import datetime
filename = "C:\\Users\\u\\.spyder-py3\\stu_andrea\\returns.csv"
# open the output file as an input file with readonly access and print all the lines
finput = open(filename, "r" ) 
count = 0
total = 0
for line in finput : 
    # 1203,10/12/2005 22:30, 478,7823, 10/12/2005 22:30
    mylist = line.split(',')
    if count == 0:
        print ( line)
    else: 
            # '10/12/2005 22:30
            date1 = mylist[1].split(" ")
            date1 = date1[0]
            date2  = mylist[4].split(" ")
            date2 = date2[0]
            print ( date1 , date2)
            date1 = datetime.strptime(date1,'%m/%d/%Y')
            date2 = datetime.strptime(date2,'%m/%d/%Y')
            
#        pass
    count += 1
finput.close()
print ( count )







from datetime import datetime, timedelta
# make a list of customerid's
filename = "C:\\Users\\u\\.spyder-py3\\stu_andrea\\returns.csv"
customerlist = []
count = 0
finput = open(filename, "r" ) 
for line in finput :  
    mylist= line.split(",")
#    print (mylist[3]) ## print the customr id's
    if mylist[3] not in customerlist: 
        customerlist.append(mylist[3])
finput.close()
print(count) 
customerlist.sort()
#print(customerlist)

### create equal size lists: 
#customercount = [None]*len(customerlist)
customercount = [0]*len(customerlist)
customerduration = [0]*len(customerlist)
customeravg = [0]*len(customerlist)
print ( len(customerlist), len(customercount), len(customerduration), len(customeravg))
print (customerlist.index('3') )



finput = open(filename, "r" ) 
for line in finput :  
     if 'Customerid' == (line): ## skip over the header row
         pass
     else:
         mylist= line.split(",") 
         i  = customerlist.index( mylist[3] )  ## mylist[3] is the customerid, find where is it in the customerlist
         customercount[i] = int( customercount[i] ) +1  
         try:
             daterented = datetime.strptime(mylist[1], '%m/%d/%Y %H:%M')
             datereturned = datetime.strptime(mylist[4], '%m/%d/%Y %H:%M')
             customerduration[i] = customerduration[i] + (datereturned-daterented).days
         except:
             pass
finput.close()

for i in range(1,len(customeravg)-1 , 1) :
    try: 
        customeravg[i] = customerduration[i]/customercount[i]
    except:
        pass
for i in range(1,len(customeravg)-1 , 1) :
    if customerlist[i] =='190':
        print (customerlist[i], " :avg: " , customeravg[i], " :count: " , customercount[i], "", customerduration[i])
    if customeravg[i] > 7 :
        print (customerlist[i], " :avg: " , customeravg[i], " :count: " , customercount[i], "", customerduration[i])

"""
mexico,cvs

How many people were born per year
For everymonth, How many people have birthdays are there
How many people are on the file
how many birthdays are missing
"""
from datetime import datetime, timedelta
############## initialse
filename = "C:\\Users\\u\\.spyder-py3\\stu_andrea\\mexico.csv"
count = filecount = 0
months = [0,0,0,0,0,0,0,0,0,0,0,0]
allyears = []
years = []
for i in range (1921, 2021, 1 ):
    allyears.append(i)
    years.append(0)
############# loop the file to add:
# births per  the month
# births per year 
# total records
# total dates
# total missing dates
finput = open(filename, "r" ) 
for line in finput :  
    filecount = filecount+1 # count the records
    mylist= line.split(",")
    mydate = mylist[3]
    ## get the years 
    ## get the months and accummulate into the months list to count the number of births in a month
    if mydate > '' and mydate.find('/') > 0 :
        count = count + 1 # count the dates
        ## find the year from the date
        if mydate[-3] == '/' :
            birthdate = datetime.strptime(mylist[3].strip(), '%d/%m/%y')
        else:
            birthdate = datetime.strptime(mylist[3].strip(), '%d/%m/%Y')
        myyear    = birthdate.year
        if myyear > datetime.today().year :
            myyear = myyear - 100
        ## count the births per year , accummulate the count per year
        i = allyears.index(myyear)
        years[i] = years[i] +1
        # count the births per month
        mymonth   = birthdate.month
        months[mymonth-1] = months[mymonth-1] + 1 

finput.close()
print ('\nnumber of people: ', filecount )
print ('\ndate count: ' , count)
print ('\nnumber of missing birthdays: ', (filecount - count))
print ("\n")
for i in range ( len(years) ):
    if years[i] >0 :
        print ('Year', allyears[i], 'Births', years[i])
print ("\n")
for i in range ( len(months) ):
    print ('Month', i, 'Births', months[i])
    
#print (months, len(months))
#n = 0
#for i in range ( 0, len(months),1):
#    n = n + months[i]
#print (n)

    

### techniques
#append to a emtpy list
#create a list of a size with 0 or None
#mydate = '17/3/75'
#print ( mydate[-3])
# find the index and adda value into that index
# if year > year.today then - 100


"""
create a csv file

do 20 times:
    
    generate a random number N between 200 and 400
    loop  so many time
    calc i in range 1 to N  : i * i + the previous , accummulate all squares of 0 to N
    print the total
    how many seconds did it take
    save the start time, N, the totalsum of all prducts, and the end time, and elapsed time  in 5 columns in the cvs file

close the csv file

read and print the 20 records in the csv file

"""

filename = "C:\\Users\\u\\.spyder-py3\\stu_andrea\\intervals.csv"
finput = open(filename, "w" )
import random
count = 0
value = 0
import time
startall = time.time()
while count < 20 : 
    start = time.time()
    count = count + 1
    N = random.randint(100,400)
    for i in range (N ):
        value = value + ( i * i ) 
    end = time.time()
    print (  N , value, (end - start))
endall = time.time()
print ( endall - startall)


"""
employeeid, name, surname, date and in leave harbour, date and time arrive on platform, dateand time leave the platform, time arrive in harbour
per shift, Per employee: how long where they on the platform, how long on the outtrip, how long on the return trip for the week
monday shift 2am - 10am:
            employeeid, name, surname, duration out , duration on, duration off
       shift 10am - 18pm
       shift 18pm-2am,
per week: per employee: total hours on platform

"""

