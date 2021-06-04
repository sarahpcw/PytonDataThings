"""

Exercise
--------
movies = ['bambi', 'rambo', 'schrek', 'cinderella', 'scarface']
days   = ['mon', 'tue', 'wed' , 'sat', 'sun']

1. Generate a random integer number between 0 and 4.  # let's  say 2
import random
nr = random.randint(0,4) # integer
print ( nr )
2
Loop count < 3 and  guess != nr
    Ask someone to guess this integer number.
    #check if the number guessed is the random numner generated
        
3. If after 3 tries 
        if he is still wrong, say wrong
   else
        he can win 2 free tickets to the movie in the corresponding position.
        Say which movie he won and which day it shows

"""


import random

movies = ['bambi', 'rambo', 'schrek', 'cinderella', 'scarface']
days   = ['mon', 'tue', 'wed' , 'sat', 'sun']

nr = random.randint(0,4) # integer
print ( nr )
guess = -1
count =  0

while nr != guess and count < 3:
    guess = input('Guess a number' )
    guess = int(guess)
    count = count + 1

if guess == nr :
    print ( 'Correct , you won the movie ', movies[nr] , ' which shows on ' , days[nr] )
else: 
    print ( 'Better luck next time' )


nr = random.randint(0,4) # integer
print ( nr )

print ( 'float between 0 and 1 ', random.random() ) # random floating point number in the range (0.0, 1.0).

print ( 'float within the range', random.uniform(1.5 , 2.5)) 

print ( random.choice([0,1011,236,32839,4]))

print ( random.choice('abcde'))






