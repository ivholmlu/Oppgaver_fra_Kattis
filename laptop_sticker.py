# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:15:15 2021

@author: Ivar
"""

wc, hc, ws, hs = [int(j) for j in input().split()]

if wc - ws <= 1:
    print('0')
elif hc - hs <= 1:
    print('0')
else:
    print('1')