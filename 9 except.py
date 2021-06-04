#
#price = 10 / 0
#print ( price )
#
#
#age = input('age?')
#age = int(age)
#if age < 5 :
#    price = 1000 / age  # try this

age = -1
price = 1000
while age < 0:
    try :
        age = input('age?')
        age = int(age)
        if age < 5 :
            price = 1000 / age  # try this
            
    except ZeroDivisionError as e : 
        print ( 'error msg 1' , e)
        print ( 'error msg 2' , repr ( e ) )  # executed if the try failed and ZeroDivisionError
        age = -1
        
    except ValueError as e: 
        print ('invalid'  , e)  # executed if the try failed and ValueError
        age = -1
    
    except :
        print ( 'invalid input ' )  # executed if the try failed, all other errors
        
    else :  
        print (' the price is :', price)       # executed if the try succeeded

   
