# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:00:37 2021

@author: KushagraK7
"""

print("You will be asked to enter two numbers.")

print("Then the computer will swap the values of the variables storing them")


A = int(input("Enter a number to store in variable 'A' "))

B = int(input("Enter a number to store in variable 'B' "))

print("Before swapping:")
print(" A = ", A, " B = ", B)

A, B = B, A

print("After swapping:")
print(" A = ", A, " B = ", B)