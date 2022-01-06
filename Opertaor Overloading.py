# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 00:03:42 2021

@author: shrey
"""

#Operator Overloading
class A:
    def __init__(self,x):
        self.x=x
        
   
class B:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return (self.x + other.x)
  
    
a=A(100)
b=B(200)
c=a+b
print(c)
