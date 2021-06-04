#finput = open("/Users/Rav/Desktop/Training/TradeClients2.csv", "r", encoding="ISO-8859-1")
#fout = open ("C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\TradeLondon.csv", "w" ) 


import os
print ( os.path )
print ( os.getcwd() ) 
print('__name__:    ', __name__)
#To get the base path of your Python working directory with the os.path method, 
#write the following within your Python file or shell:

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
print(BASE_DIR)
#However, to use the above method to check the active working directory, type the following:

import os
CURR_DIR = os.path.dirname(os.path.realpath(__name__))
print(CURR_DIR)


print('basename:    ', os.path.basename(__name__))
print('dirname:     ', os.path.dirname(__name__))

myfile =  os.getcwd() 
import os
if os.path.exists(myfile+"\\TradeLondon.csv"):
    print ( " File is there " )
else:
    print ( " File is not there " )
    

import os
if os.path.exists("C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\test.bd"):
    print ( " File is there " )
else:
    print ( " File is not there " )


filename = "C:\\Users\\u\\.spyder-py3\\3W-Webinar\\movies4.txt" #########3
fout = open(filename, "w" )  #############

movies = ['bambi', 'rambo', 'shrek', 'rocky','skyfall','casino','cinderella']
days   = ['mon'  , 'tue'  , 'wed','thu','fri','sat','sun' ]
stopvalue = len ( movies )
#use a for loop to iterate the list, using an integer i and uding it as an index
for i in range ( 0, stopvalue , 1 ):
    print ( days[i]+ ',' + movies[i] +'\n' ) 
    line = days[i]+ ',' + movies[i] +'\n'
    fout.write(line)  ########
fout.close() ###########

finput = open(filename, "a" ) 
finput.write('sat,rocky\n')
finput.close()

finput = open(filename, "r" ) 
count = 0
day = input("Which day would you like to go to the movies?")
for line in finput : 
    # 1,234,353453,iuoq, fjpwjefpw
    mylist = line.split(',')  #  ['1','234','353453','iuoq', 'fjpwjefpw']
    if mylist[0] == day :
        print (mylist[0],mylist[1])  
    count += 1
print ( 'movies', count)
finput.close()






movies = ('mon,bambi,10','tue,Rambo,12','wed,shrek,15') 

filename = "C:\\Users\\u\\.spyder-py3\\3W-Webinar\\movies4.csv"
 
fout = open(filename, "w" ) 

count = 0 
for movie in movies : 
        movie = movie + '\n'
        fout.write(movie)
        count = count + 1
print ( count)
fout.close()

finput = open(filename, "a" ) 
finput.write('sat,rocky,12' + '\n')
finput.close()

m = input ("which movie? ")
finput = open(filename, "r" ) 
count = 0
for line in finput :
#        print (line )
        mylist = line.split(",")
#        print(mylist)
        value = mylist[1]
        if value == m:
            print ("Your preferred movie", mylist[1], "shows on", mylist[0])
finput.close()


finput = open("C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\TradeClients2.csv", "r" ) 
count = 0
for line in finput : 
#    print (line)  #  Hotel,  Other, #Wholesaler, #Non-member, Educational, Wine Bar, Agent, Key Retail Buyer
    count += 1
print ( 'Trade clients', count)
finput.close()

#
finput = open("C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\BaseballPlayers.csv", "r" ) 
count = 0
countF = 0
for line in finput :
    if 'Freddy Garcia' in line:   #Freddy , David, John
        print (line)
        countF += 1
        
    count += 1
print ( 'Baseball', count, countF)
finput.close()







 






















""" for mac
finput = open("/Users/user/.spyder-py3/movies4.txt", "r")
'~/Desktop/somefolder/movie_quotes.txt'

import os
f = open (os.path.expanduser("~/Desktop/somedir/somefile.txt"))

fOut = open("/Users/szucszsuzsanna/Desktop/spyder/movies4.csv", "w")
line = 'THU'
fOut.write(line)
fOut.close()

"""
 


#fOut.close()
#loc = ("TradeClients.csv") 
#fOut = open("rambo.csv", "w")	
#fIn = open(loc, "r")				#open the file to read it
#for line in fIn:						#loop all record
#    l = line.split(',')
#    print ( l[9], l[8])
#    if "wholesales" in line:
#        print ( line )
#fOut.close()        
#fIn.close()						#close the file

#fAppend = open("movies.csv", "a")			#open the file with a to append
#line='wed,rocky,10,action\n'
#fAppend.write(line)					#append a new value
#fAppend.close()	
#
#movies = []
#fIn = open("movies4.csv", "r")				#open the file to read it
#for line in fIn:						#loop all record
#    movies.append(line)		 
#fIn.close()	
#
#numberPeople = 10
#for movie in movies :
#    m = movie.split(',')
#    if m[1] == "rambo":
#        print (m[1],'screens on ', m[0])
#        print ('the ticketprice is $%s' % m[2])
#        t = numberPeople * float(m[2])
#        print ('for %d people, the ticketprice is $%.2f' % (numberPeople,t))
