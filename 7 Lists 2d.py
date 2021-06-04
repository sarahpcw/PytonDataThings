
people = [   ['peter'      , 'sally' , 'jones' , 'mary']  ,  
             ['birmingham' , 'leeds' , 'bath'  , 'ascot'] ,
             ['driver'     , 'actor' , 'nurse' , 'actor']    ]
# peter birmingham driver
# sally leeds actor
# jones bath nurse
# mary ascot actor

print ( ' number of rows', len(people))   # number of rows

print (  'number of columns', len(people[0]) , people[0]) #number of columns in row 0 #How many elements in row [0]: 
print ( len(people[1]) , people[1]) #number of columns in row 1 #How many elements in row [1]: 
print ( len(people[2]) , people[2]) #number of columns in row 2 #How many elements in row [2]: 

for row in range(0, len(people) , 1 ):
    print ( people[row])
    
    
    
#Referring to individual elements
print (' peter : ' , people[0][0])  # row column
print (' sally : ' , people[0][1])
print (' jones : ' , people[0][2])
print (' mary : '  , people[0][3])


for row in range(0, len(people) , 1 ):
    print ( people[row])
    for i in range ( 0 , 4 , 1):  #0,1,2,3
        print ( 'for row ', row, ' i is: ', i , end = "  " ) 
        #  0 , i: 0,
    print ( "")

for i in range ( 0 , len(people[1]) , 1):
    print ( people[1][i],  end =  "  " ) 
print ( "")

for i in range ( 0 , len(people[2]) , 1):
    print ( people[2][i].ljust(10) ,  end = "  ") 
print ( "")










###Nested Loop
for row in range( 0, len(people) , 1):
    for i in range ( 0 , len(people[row]) , 1):
        print ( people[row][i].ljust(11),    end ="  ") 
    print ( "")


people = [   ['peter'      , 'sally' , 'jones' , 'mary']  ,  
             ['birmingham' , 'leeds' , 'bath'  , 'ascot'] ,
             ['driver'     , 'actor' , 'nurse' , 'actor']    ]




print (len(people))   # number of rows
print (len(people[0])) # number of columns

for col in range( 0, len(people[0]) , 1):
    for row  in range ( 0 , len(people) , 1):
        print ( people[row][col].ljust(11),    end ="  ") 
    print ( "")


movies = [   ['bambi' , 'rambo' , 'shrek' , 'rocky']  ,  
             ['mon'   , 'tue'   , 'wed'  , 'thu'] ,
             ['family', 'action' , 'family' , 'drama']    ]

for col in range( 0, len(movies[0]) , 1):
    for row  in range ( 0 , len(movies) , 1):
        print ( movies[row][col] ,    end ="  ") 
    print ( "")






people = [   [''      ,''      ,''      ,''      ],  
             [''      ,''      ,''      ,''      ], 
             [''      ,''      ,''      ,''      ] ]
# get values from enduser
for row in range( 0, len(people) , 1):
    if row == 0:
        values = "names"
    elif row == 1:
        values = "cities"
    else: 
        values = "jobs"
    print ( "Please enter the values for ", values)
    for i in range ( 0 , len(people[row]) , 1):
            people[row][i] = input("your value?")
    print ( "")


###Nested Loop
for col in range( 0, len(people[0]) , 1):
    for row in range ( 0 , len(people) , 1):
        print ( people[row][col].ljust(11),    end ="  ") 
    print ( "")
    
###Nested Loop
for row in people:
    for element in row:
        print (element.ljust(11),    end ="  ") 
    print (' ')
    


    
##
for row  in people:
    for x in row:
               print (x, '\t', end=" ")
    print ("\n")      		 
    
    
    
#"""
#peter dover driver
#sally leeds actor 
#"""
rows = len(people)  # 3
cols = len(people[0]) # 4
for col in range ( 0 , cols ):
    for row in range ( 0, rows ) :
        print (people[row][col].ljust(10), end=" ")
    print ('')