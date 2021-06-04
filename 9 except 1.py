
#https://docs.python.org/2/library/exceptions.html
#
i = 0 
while i == 0 :
    try : 
        i = int ( input ('please give a number but not 0 '))
        
    except ValueError as e: 
        print ( 'error msg 1' , e)
        print ( 'error msg 2', repr (e) )
    
    except : 
        print ('please enter a valid integer')
        
#    
print (i)
