## -*- coding: utf-8 -*-
##String vs List vs Tuples
##string variable
#str = 'Hello World!'	#using a string variable
#print (str)          		# Prints complete string
#print (str[0])       	# Prints first character of the string
#print (str[2:5])     	# Prints characters starting from 3rd to 5th
#print (str[2:])     		# Prints string starting from 3rd character
#
##List
#list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
#tinylist = [123, 'john']
#print (list)        		# Prints complete list
#print (list[0])   		# Prints first element of the list
#print (list[1:3])  		# Prints elements starting from 2nd till 4th 
#print (list[2:])     		# Prints elements starting from 3rd element
#print (list + tinylist) 	# Prints concatenated lists
##tuple
#tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
#tinytuple = (123, 'john')
#print (tuple)         	# Prints complete list
#print (tuple[0])        	# Prints first element of the list
#print (tuple[1:3])      	# Prints elements starting from 2nd till 3rd 
#print (tuple[2:] )      	# Prints elements starting from 3rd element
#print (tuple + tinytuple) 	# Prints concatenated lists
##Update is Invalid with tuple: 
## tuple[2] = 1000   		 # Invalid syntax with tuple 
#list[2] = 1000   			 # Valid syntax with list
#print (list) 
#invalid functions with tuple
#append, remove, del, sort and reverse cannot be done with a tuple 
#Valid:
moviesTuple = ( 'bambi', 'rambo', 'schrek')
moviesList = [ 'bambi', 'rambo', 'schrek' ]
print(type ( moviesList) ) 
print(type ( moviesTuple) ) 

for movie in moviesTuple: 
    print ( movie )

for i  in range ( len( moviesTuple) ) : 
    print ( moviesTuple[i] )

print ( moviesTuple[0:2])
print ( moviesTuple[0:])
print (moviesTuple)
moviesTuple[0] = 'kiwi'
moviesList.sort()
print (moviesList)                 #sort the list


#moviesTuple[0] ='cinderella'
moviesList = list(moviesTuple )
print ( type ( moviesList) )
moviesTuple = tuple(moviesList)



"""
days = ('mon', 'tue', 'wed' )
tup3 = (movies + days)
print (tup3)
movies = (movies + days)
print (movies)
movies = tuple(movies) #convert
print (movies)
movies = list(movies) #convert
movies[0]='MANGO'
print (movies)
"""