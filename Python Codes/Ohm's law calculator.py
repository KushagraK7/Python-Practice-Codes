# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:34:25 2021

@author: KushagraK7
"""

print("")
print("Ohm's law")
print("Enter any two of the values and the third one will be calcuated")
print("")

while(1):
    print("")
    print("")
    print("For entering voltage, press 'V'")
    print("For entering current, press 'I'")
    print("For entering resistance, press 'R'")
    print("Press 'E' to exit")
    
    ch = input("Press the suitable key from above and hit Enter ")
    
    if(ch == 'V' or ch == 'v'):#If voltage is entered
        v = float(input("Enter the voltage "))
        while(1):
            print("")
            print("For voltage = ", v, "volts")
            print("")
            print("For entering current, press 'I'")
            print("For entering resistance, press 'R'")
            print("For going back to main menu, press 'M'")
            
            ch = input("Press the suitable key from above and hit Enter ")
            
            if(ch == 'R' or ch == 'r'):#If resistance is entered, cal current
                r = float(input("Enter the resistance value "))
                i = v/r
                
                print("")
                print("    The current is ", i, " amps")
                print("")
                
            if(ch == 'I' or ch == 'i'):#If current is entered, cal resistance
                i = float(input("Enter the current value "))
                r = v/i
                
                print("")
                print("   The resistance is ", r, "Ω")
                print("")
                
            if(ch == 'M' or ch == 'm'): break
                
    if(ch == 'I' or ch == 'i'):#If current is entered
        i = float(input("Enter the current "))
        while(1):
            print("")
            print("For current = ", i, "amps")
            print("")
            print("For entering voltage, press 'V'")
            print("For entering resistance, press 'R'")
            print("For going back to main menu, press 'M'")
            
            ch = input("Press the suitable key from above and hit Enter ")
            
            if(ch == 'V' or ch == 'v'):#If voltage is entered, cal resistance
                v = float(input("Enter the voltage value "))
                r = v/i
                
                print("")
                print("   The resistance is ", r, "Ω")
                print("")
                
            if(ch == 'R' or ch == 'r'):#If resistance is entered, cal voltage
                r = float(input("Enter the resistance value "))
                v = i*r
                
                print("")
                print("   The voltage is ", v, "volts")
                print("")
                
            if(ch == 'M' or ch == 'm'): break
                
    if(ch == 'R' or ch == 'r'):#If resistance is entered
        r = float(input("Enter the resistance "))
        while(1):
            print("")
            print("For resistance = ", r, "Ω")
            print("")
            print("For entering voltage, press 'V'")
            print("For entering current, press 'I'")
            print("For going back to main menu, press 'M'")
            
            ch = input("Press the suitable key from above and hit Enter ")
            
            if(ch == 'V' or ch == 'v'):#If voltage is entered, cal current
                v = float(input("Enter the voltage value "))
                i = v/r
                
                print("")
                print("   The current is ", i, " amps")
                print("")
                
            if(ch == 'I' or ch == 'i'):#If current is entered, cal voltage
                i = float(input("Enter the current value "))
                v = i*r
                
                print("")
                print("   The voltage is ", v, "volts")
                print("")
                
            if(ch == 'M' or ch == 'm'): break
                
    if(ch == 'E' or ch == 'e'): break