# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:38:01 2021

@author: Ivar
"""

n = int(input())

QALY = 0

for i in range(n):
    i = input()
    i = i.split()
    i = list(map(float, i))
    QALY += (i[0])*(i[1])

print(QALY)

# 5
# 1.0 12.0
# 0.7 5.2
# 0.9 10.7
# 0.5 20.4
# 0.2 30.0