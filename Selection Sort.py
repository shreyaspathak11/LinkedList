# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:58:03 2021

@author: shrey
"""

def sort(list):
    for i in range(len(list)-1):            #Loop1
        minpos = i
        for j in range(i,len(list)):        #loop2
            if list[j]<list[minpos]:
                minpos=j 
        
        temp=list[i]                    #SWAP
        list[i]=list[minpos]
        list[minpos]=temp
        
      
list=[5,3,8,7,6,2]
sort(list)
print(list)
