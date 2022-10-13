# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:52:13 2021

@author: Ivar
"""

N = 10

for i in range (N):
    i = int(input())
    if i == -1:
        break
    distance = 0
    tid = 0
    if i == -1:
        break
    for j in range(i):
        speed_time = input().split()
        distance += int(speed_time[0])*(int(speed_time[1])-tid)
        tid = int(speed_time[1])
    print(f'{distance} miles')
        
        
        
    

    
    