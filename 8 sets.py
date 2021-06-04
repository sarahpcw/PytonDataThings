# -*- coding: utf-8 -*-
"""
list: l = ['','','']
tuple: cannot change t = ('','','')
Set : unordered , unique values
set() method is used to convert any 
of the iterable to sequence of iterable elements 
with dintinct elements, commonly called Set

"""

days = [  'mon', 'wed', 'thu', 'thu', 'sat']
print ( days)

myset = {'a','b','c'}
print(myset)
myset.add('p')
for s in myset:
    print (s)
#
daysset = set(days)
print (daysset) # removes thursday but scrambles the order
#
## use list functions to correct the list to show all the days of the week
#print (myset[0])  # set does support indexing
##
myset[0]='x'  # cannot change values
#
myset = {'x','b','c'}  # can recreate
print(myset)

mylist = list (myset)
mylist.sort()
print (mylist)

"""
add() and remove() 
"""