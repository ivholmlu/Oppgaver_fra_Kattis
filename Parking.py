# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:33:44 2021

@author: Ivar
"""

"""
Gjennomsnittet av input, summen av alle differansene

"""

N = int(input())

for i in range(N):
    n = int(input())
    sum1 = 0
    dist = 0
    parkeringer = [int(j) for j in input().split()]
    for l in parkeringer:
        sum1 += (l)
        
    
    dist += abs(sum1/n - min(parkeringer))
    dist += max(parkeringer) - min(parkeringer)
    dist += max(parkeringer) - sum1/n
    print(f'{dist:.0f}')
        
        