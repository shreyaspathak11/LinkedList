# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:26:16 2021

@author: shrey
"""

class A:
    def __init__(self,m):
        self.work=m
        print("class A Constructor")
    def show(self):
        print("Class A ::show")
class B(A):
    def display(self):
        print("class B display",self.work+100)
        
s=B(1000)
print(s.work)
s.show()
s.display()
