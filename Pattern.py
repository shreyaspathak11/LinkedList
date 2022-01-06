# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:16:54 2021

@author: shrey
"""

def pattern(n):
    for i in range(0,n):
        print()
        for j in range (n-i):
            print('*', end=" ")
            
         
            
def pattern2(k):
    for i in range(0,k):
        for j in range(i+1):
            print("*", end=" ")
        print()
        
        
        
z=int(input("Enter  :"))   
pattern(z)
print()         
pattern2(z)