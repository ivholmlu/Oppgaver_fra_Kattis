# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:52:10 2021

@author: Ivar
"""

"""
Dobbel for løkke med if test?

Link: https://open.kattis.com/problems/anotherbrick

"""


line = input()
line = line.split()

height = int(line[0])
width = int(line[1])
amountbricks = int(line[2])
bricksizes = input()
bricksizes = bricksizes.split()
bricksizes = list(map(int, bricksizes))
width_now = 0
height_now = 0

for brick in bricksizes:
    
    if width_now != width:
        width_now += brick
        if width_now > width:
            print('NO')
            break
    
    if width_now == width:
        height_now += 1
        width_now = 0
        if height_now == height:
            print('YES')
            break

        
# 2 10 7
#5 5 5 3 5 2 2
        
    

    
    

    
    
    
    
    
