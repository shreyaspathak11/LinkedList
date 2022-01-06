# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:18:11 2021

@author: shrey
"""
pos=0
def search(list,n):
    x=len(list)
    for i in range(0,x):
        if list[i]==n:
            globals()['pos']=i
            return True
    else:
        return False
    
    
    
    
list=[2,4,5,3,11,6,9,43]
n=int(input("Enter the no. to search for: "))
if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")    