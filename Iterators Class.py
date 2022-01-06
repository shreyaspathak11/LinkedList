# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:01:30 2021

@author: shrey
"""
n=int(input("ENTER : "))
class TopTen:
    def __init__(self):
        self.num=1
    
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.num<=n:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values= TopTen()

for i in values:
  print(i)          
    