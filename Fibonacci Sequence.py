# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:46:29 2021

@author: shrey
"""
def fib(n):
    a=0
    b=1
    i=2
    print(a)
    print(b)
    while i<n:
        c=a+b
        
        
        a=b
        b=c
        i=i+1
        
        print(c," ")
        



fib(10)