# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:12:20 2021

@author: Ivar
"""

N = int(input())
sum1 = 0
b = input()
b = b.split()
b = list(map(int, b))

for i in b:
    sum1 += i


print(sum1)