# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:10:42 2021

@author: Ivar
"""




C = float(input())

L = int(input())

pris = 0

for i in range(L):
    w, l = [float(j) for j in input().split()]
    areal = w*l
    pris += areal *C

print(f'{pris:.8f}')









