# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:58:14 2021

@author: shrey
"""
nums=[3,5,7,9]
it=iter(nums)
print(it.__next__())
print(next(it))

for i in nums:
    print(next(it))