# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:37:18 2021

@author: shrey
"""
pos=0
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=((l+u)//2)
        if list[mid]==n:
            globals()['pos']=mid
            return True
            
        else:
            if list[mid]<n:
                    l=mid+1
            else:
                    u=mid-1
    
    return False #Jab kuch na mile tab!


list=[1,2,3,4,5,6,7,8,9,11,22,34,53,54,55,303]
n=int(input("Enter the No. wanna search:  "))

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
    
    
    
    