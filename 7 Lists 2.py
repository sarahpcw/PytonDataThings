"""
#Lesson 7: More about lists – insert, append, remove, delete,  sort,  reverse

"""

movies = [  'bambi', 'rambo', 'schrek']
#print('\n', movies, 'length: ', len(movies))

movies[0] = 'MANGO'				#update a value, using the index
print('\n', movies, 'length: ', len(movies))
#
movies.insert(2, 'watermelon')  #insert an element
print('\n', movies, 'length: ', len(movies))

movies.insert(2,'WATERMELON')     #remove an element using a value , case sensitive
print('\n', movies, 'length: ', len(movies))
#
movies.append('kiwi')           #append an element
print('\n', movies, 'length: ', len(movies))

movies.remove('WATERMELON')     #remove an element using a value , case sensitive
print('\n', movies, 'length: ', len(movies))
#
del movies[0]                   #delete an element using an index	
print('\n', movies, 'length: ', len(movies))
#
movies.sort()                   #sort the list
print('\n', movies, 'length: ', len(movies))
#
movies.reverse()                #reverse the list
print('\n', movies, 'length: ', len(movies))


price  = [10,11,32,13,54,15,16]
price.sort()  
price.reverse()                #reverse the list
print('\n', price, 'length: ', len(price))


days = ["Mon","Mon","Wed","Fri","Fri","Sat"]
days.remove("Mon")
print(days)






