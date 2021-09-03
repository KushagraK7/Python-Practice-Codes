# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:17:16 2021

@author: KushagraK7
"""

n = int(input("Please enter number "))

nn = n

if(n < 0): n = n*(-1)#If no is -ve, convert it to +ve before testing

while(n >0):
    n-=2
    
    
if(n): print(nn, "is odd")

else: print(nn, "is even")
