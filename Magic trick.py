# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:53:08 2021

@author: Ivar
"""

"""
Hvis to like bokstaver,
print 0, ellers print 1
"""

tall = input()
oversikt = {}
a = 0
for i in tall:
    if i in oversikt:
        print('0')
        a = 1
        break
    else: 
        oversikt[i] = 0
    
if a != 1:
    print('1')


    