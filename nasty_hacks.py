# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:04:56 2021

@author: Ivar
"""

N = int(input())
for n in range(N):
    inntekt, inn_mrek, rekl = [int(j) for j in input().split()]
    if inntekt> inn_mrek - rekl:
        print('do not advertise')
    elif inntekt == inn_mrek - rekl:
        print('does not matter')
    else: 
        print('advertise')