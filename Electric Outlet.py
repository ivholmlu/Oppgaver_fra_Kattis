# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:14:04 2021

@author: Ivar
"""

"""
Starter med 1 uttak, avslutter med alle utganger.
Derfor vil utakkene starte med = 2
"""

N = int(input())

for i in range(N):
    verdier = [int(j) for j in input().split()]
    antall = verdier[0]
    sum1 = 0
    for k in verdier[1:]:
        sum1 += k
    print(sum1-antall+1)
    
    
    