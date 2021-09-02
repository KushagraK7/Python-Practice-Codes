# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
while 1:
    
    print("Enter C to convert Celcius to Farenheit")
    print("Enter F to convert Farenheit to Celcius")
    print("Enter E to exit")
    
    ch = input("Enter your coice and press Enter ")
    
    if(ch == 'C' or ch =='c'):
        print(" ")
        print("Degree Celsius to Farenheit")
        print(" ")
        c = float(input("Please enter the temperature "))
        
        ft = c*(9/5)+32
        
        ft = round(ft, 1)
        
        print(" ")
        print(" Temperature is", ft, "degrees Farenheit")
        print(" ")
    
    if(ch == 'F' or ch =='f'):
        print(" ")
        print("Farenheit to Degree Celsius")
        print(" ")
        fc = float(input("Please enter the temperature "))
        
        c = (fc - 32)*(9/5)
        
        c = round(c, 1)
        
        print(" ")
        print(" Temperature is", c, "degrees Clesius")
        print(" ")
        
    if(ch == 'E' or ch =='e'): break
    


