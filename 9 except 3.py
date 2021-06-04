#user_input = int ( input ('Enter a number: ')  )
#print ( user_input )


user_input = -1


while user_input == -1:
    try:
        user_input =  int ( input ('How many adults: ')  ) 
    except ValueError as e:  # if error  / exception
        print ('Invalid input, the value remains at default', user_input)  # abc... %^&* ten
        print (e)  # abc... %^&* ten
    except :
        print ('all other get')
        
user_input = user_input * 10
print ( 'Total Price for movie tickets ', user_input)
