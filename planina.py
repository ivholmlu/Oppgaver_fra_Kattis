# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:02:20 2021

@author: Ivar
"""

N = int(input())
side = 2
for i in range(N):
    side = side+side-1
    
    
print(side**2)
    
    
    