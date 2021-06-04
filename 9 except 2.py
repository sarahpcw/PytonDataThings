# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:20:24 2020

@author: u
"""


filename = "C:\\Users\\u\\.spyder-py3\\3W-Webinar\\movies4.txt"
 
try : 
    myfile = open (filename,"r")
      
      
except FileNotFoundError as e:
    
    print ( 'file not found', e)
    
    
except : 
    print ( 'catch all')


print("done")


        
        


