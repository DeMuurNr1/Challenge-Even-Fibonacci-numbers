# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def FIBO():
    T     =   0
    X     =   0
    Y     =   1
    
    while X <= 4e6:
        #print(X)        #print fibonacci numbers
        if X%2==0:
            T = T + X
        X, Y =  Y, X + Y
    
    print("De sommatie van de even Fibonacci nummers = ", T)    #sumation of all even numbers
    #print("X = ", X)
    #print("Y = ", Y)
    
FIBO()
