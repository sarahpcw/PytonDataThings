movies = ['bambi', 'rambo', 'shrek', 'rocky','skyfall','casino','cinderella']
days   = ['mon'  , 'tue'  , 'wed','thu','fri','sat','sun' ]

#print all the values the whole list, aal the values
print ( movies ) 
print ( days   ) 

#print the length of the list, i.e. the count of all the values, how many values are there?
print ( len ( movies ) ) 
print ( len ( days   ) ) 

# refer to individual element using indexes ( integers in the [] indicating the position in the list)
print ( movies[0] )
print ( movies[1] )
print ( movies[2] )
# refer to individual element using indexes ( integers in the [] indicating the position in the list)
print ( "On", days[0], "the movie showing is" , movies[0] )
print ( "On", days[1], "the movie showing is" , movies[1] )
print ( "On", days[2], "the movie showing is" , movies[2] )

filename = "C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\movies4.csv" #txt

movies = ['bambi', 'rambo', 'shrek', 'rocky','skyfall','casino','cinderella']
days   = ['mon'  , 'tue'  , 'wed','thu','fri','sat','sun' ]

print ( len ( movies ))

for i in range ( 0, 7 , 1):
    print (movies[i])


stopvalue = len ( movies )
#use a for loop to iterate the list, using an integer i and uding it as an index
for i in range ( 0, stopvalue , 1 ):
    print ( days[i]+ ',' + movies[i] ) 
 
"""
mon, bambi
tue, rambo
wed, shrek
"""    
    
    
    
    
    
    
    
    
#use a for loop to iterate the list, use the integer as an index to refer to values at specific positions
for i in range ( 0, len(movies) , 1 ):
    if movies[i] == 'rambo':
        print ( days[i], movies[i], i ) 
#shortcut loop for a list, looping all the values, but without the position of values
for movie in movies:
    print ( movie )
    
for m in movies:
    print ( m ) 
    
movies = ['bambi', 'rambo', 'shrek', 'rocky','skyfall','casino','cinderella']
days   = ['mon'  , 'tue'  , 'wed','thu','fri','sat','sun' ]
price  = [10,11,12,13,14,15,16]
print ("Day", "Movie".rjust(11), "Price")
print ("---", "-----------".rjust(11), "-----")
for i in range ( 0, len(movies) , 1 ):
    print ( days[i], movies[i].rjust(11), price[i] )    
 

  
    
