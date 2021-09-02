# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:20:25 2021

@author: Lenovo
"""

q = 1

while q:
    
        print("Simple interest calculator")
        print("")
        print("Here, we are going to use the formula P*R*T/100 to calculate the interest")
        print("Here, 'P' is priciple, 'R' is rate if interest and 'T' is time")
        p = float(input("Start by letting us know the principle amount(P) "))
        print("")
        r = float(input("Next, tell us the rate of interest(R) "))
        print("")
        t = float(input("Lastly, share the time period(T) "))
        print("")
        
        si = p*r*t/100
        
        print("The calculated interest has come to be ", si)
        print("")
        ch = input("Enter in 'A' to calculate again, press just Enter to exit ")
        
        if(ch == 'A' or ch == 'a'): q = 1
        else: q = 0
        
        