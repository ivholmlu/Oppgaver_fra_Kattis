# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:51:08 2021

@author: Ivar
"""

"""
Hvordan finne max og min APBM


link : https://open.kattis.com/problems/heartrate
"""

N = int(input())

for i in range(N):
    i = input().split()
    b = int(i[0])
    p = float(i[1])
    t = (b/p)
    BPM = (60*b)/p
    APBM = 60/t
    print(BPM)
    print(APBM)
    
    