# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:34:25 2021

@author: KushagraK7
"""

i = -1
v = -1
r = -1
ch = 'a'

print("Ohm's law")
print("Enter any two of the values and the third one will be calcuated")

while(ch != 'E' or ch != 'e'):
    print("For entering voltage, press 'V'")
    print("For entering current, press 'I'")
    print("For entering resistance, press 'R'")
    
    ch = input("Press the suitable key from above and hit Enter ")
    
    if(ch == 'V' or ch == 'v'):#If voltage is entered
        v = float(input("Enter the voltage "))
        while(ch != 'I' or ch != 'i' or ch != 'R' or ch != 'r'):
            print("For entering current, press 'I'")
            print("For entering resistance, press 'R'")
            
            ch = input("Press the suitable key from above and hit Enter ")
            
            if(ch == 'R' or ch == 'r'):#If resistance is entered, cal current
                r = float(input("Enter the resistance value "))
                i = v/r
                
                print("The current is ", i, " amps")
                
            if(ch == 'I' or ch == 'i'):#If current is entered, cal resistance
                i = float(input("Enter the current value "))
                r = v/i
                
                print("The resistance is ", r, "Ω")
                
                
        if(ch == 'I' or ch == 'i'):#If current is entered
            v = float(input("Enter the voltage "))
            while(ch != 'V' or ch != 'v' or ch != 'R' or ch != 'r'):
                print("For entering voltage, press 'V'")
                print("For entering resistance, press 'R'")
                
                ch = input("Press the suitable key from above and hit Enter ")
                
                if(ch == 'V' or ch == 'v'):
                    r = float(input("Enter the voltage value "))
                    i = v/r
                    
                    print("The current is ", i, " amps")
                    
                if(ch == 'I' or ch == 'i'):
                    i = float(input("Enter the current value "))
                    r = v/i
                    
                    print("The resistance is ", r, "Ω")