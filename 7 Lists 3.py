movies = [  'bambi', 'RAMBO', 'schrek', 'cinderella']
# How to loop
for x in range (0 , len(movies) , 1):
     print ( movies [x])  # access to the index x as well as value movies[x]

# How to loop 
for movie in movies:
    print ( movie )   # cannot the positions or indexes of the values 

movie = input ( "which movie? ")   
# How to find a value
if movie.lower() in movies: 
    print ( 'rambo is a value found in the list movies')
else:
    print ( 'rambo not in list')


# How to find a value
if 'rambo' not in movies: 
    print ( 'rambo not in list movies')

 
# How to find a value
movie = input ( "which movie? ")
for x in range (0 , len(movies) , 1):
    if movies[x].lower() ==movie.lower():
        print ( movies [x] )  # access to the index x as well as value movies[x]

 # How to find a value
for movie in movies:
    if movie == 'rambo':
        print ( movie )   # cannot the positions or indexes of the values 