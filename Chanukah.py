# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:56:01 2021

@author: Ivar
"""

"""


"""

N = int(input())
candles = 0
for k in range (1, N+1):
    i = input().split()
    j = int(i[1])
    l = int(i[0])
    candles += j
    
    for m in range(1, j+1):
            candles += m

    print(k, candles)
    candles = 0
    
    