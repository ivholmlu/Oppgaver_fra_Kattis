# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:15:33 2021

@author: Ivar
"""


"""
Ikke full pott
Vet ikke hvorfor


"""


line = input().split()
h = int(line[0])
P= int(line[1])
K_lamp = 60
n = 1
K_bulb = 5
for i in range(1, 8001):
    K_lamp += ((11 * h* P)/100000)

    K_bulb += ((60 * h * P)/100000)
    if K_bulb > K_lamp:
        print(i)
        break
    if i * h > n*1000:
        K_bulb += 5
        n+=1
        
    



