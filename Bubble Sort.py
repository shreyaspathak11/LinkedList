# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:49:00 2021

@author: shrey
"""

def sort(list):
    for i in range (len(list)-1,0,-1):            #loop 1:
       for j in range(i):                         #loop 2:
        
            if list[j]>list[j+1]:
            
                temp=list[j]                       #Swapping
                list[j]=list[j+1]
                list[j+1]=temp

list=[5,3,8,6,7,2]
sort(list)
print(list)



