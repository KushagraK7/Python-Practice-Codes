# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:31:44 2021

@author: KushagraK7
"""

print("Kilogram to Pound converter")

while 1:
    
    print("Enter K to convert Kilogram to Pounds")
    print("Enter P to convert Pounds to Kilogram ")
    print("Enter E to exit")
    
    ch = input("Enter your coice and press Enter ")
    
    if(ch == 'K' or ch =='k'):
        print(" ")
        print("Kilogram to Pound")
        print(" ")
        kg = float(input("Please enter the weight "))
        
        p = kg*2.2
        
        p = round(p, 1)
        
        print(" ")
        print(" Weight is", p, "pounds")
        print(" ")
    
    if(ch == 'P' or ch =='p'):
        print(" ")
        print("Pound to Kilogram ")
        print(" ")
        p = float(input("Please enter the weight "))
        
        kg = p/2.2
        
        kg = round(kg, 1)
        
        print(" ")
        print(" Temperature is", kg, "Kilograms")
        print(" ")
        
    if(ch == 'E' or ch =='e'): break