# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:18:47 2021

@author: shrey
"""

class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is : ",self.cpu,self.ram)
com1=computer('i5',16)
com2=computer('rygen-3',8)

com1.config()
com2.config()
