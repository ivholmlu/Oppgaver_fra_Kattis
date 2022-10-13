# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:24:01 2021

@author: Ivar
"""

N = int(input())

for i in range(N):
    i = input()
    if 'Simon says' == i[0:10]:
        print(i[11:])
    

