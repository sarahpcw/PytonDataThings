mylist = [("rambo","bambi","schrek"), ("mon","tue","wed"), [23,34,45]]
for row in range ( 0 , len(mylist), 1):
    for i in range( 0, len(mylist[row]), 1 ):      # the increment value 1 is omitted, and it defaults to 1
        print ( mylist [row][i] , end =" "  )
    print ("\n")
mylist[2][0] = 999

movies = ('bambi','rambo','shrek') 

print ( movies[0])
print ( movies[1])
print ( movies[2])

for i in range( 0, 3 ):      # the increment value 1 is omitted, and it defaults to 1
    print ( movies [i], i  )
#    
for movie in movies:
    print (movie)
#
movies[2] = "ROCKY"     # assignment invalid
# append, del, remove, insert, sort and reverse invalid for tuples

movies.append(34)
##
mylist2 = list(movies)
mylist2[2]= 304
movies = tuple(mylist2)
print ( movies)
