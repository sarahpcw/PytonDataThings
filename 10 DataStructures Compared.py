import pandas as pd
import numpy as np

# print head and tail of Series
s = pd.Series(np.random.randn(100))  # 10 random numbers
print (s)
print (s.head(5))
print (s.tail())

s1=pd.Series(np.random.randn(10))# get 10 numbers
print('------------s1---------------')
print('s1[0]',s1[0])
print('s1[1]',s1[1])
print('s1[2]',s1[2:5])
print (type (s1))
#Clear, del, type, len
mydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(  mydict['Name'] )    # mylist[0]
print(  mydict['Age'] )  
print(  mydict['Class'] )  	

movies = ['bambi', 'rambo', 'shrek']
mytuple = ('bambi', 'rambo', 'shrek')
#print the length of the list, i.e. the count of all the values, how many values are there?
print ( len ( movies ) ) 
print ( movies[0] )
print ( movies[1] )
print ( movies[2] )

x = np.arange(10) 
print ('1===>>> ', x)  
print ('1===>>> ', x[2:5])     

import numpy as np
import pandas as pd
from datetime import datetime
presentime=datetime.now() 
print(" NOW THE TIME IS:",presentime)
print("Todays Date is:",presentime.strftime('%Y-%m-%d'))
print("Year is:",presentime.year)
print("Month is:",presentime.month)
print("Day is:",presentime.day)
print("-------------------")

dates = pd.date_range ('2015-02-24', periods=4, freq='MS') 
for date in dates:
     print(date)
dates = pd.date_range (presentime.strftime('%Y-%m-%d'), periods=4, freq='MS') 
for date in dates:
     print(date)
print (type(dates))

