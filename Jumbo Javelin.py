# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:44:54 2021

@author: Ivar
"""

N = int(input())
sum1 = 0

for i in range(N):
    sum1 += int(input())

sum1 -= N-1

print(sum1)
    
    