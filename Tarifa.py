# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:27:37 2021

@author: Ivar
"""

X = int(input())

N = int(input())
sum1 = 0
for i in range(N):
    i = int(input())
    sum1 += X-i
    
print(sum1+X)
    