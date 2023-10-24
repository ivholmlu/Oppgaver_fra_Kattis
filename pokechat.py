# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:22:37 2023

@author: Ivar
"""
S = input()
l = input()
indexes = [int(l[i:i+3]) for i in range(0,len(l),3)]
word = ''
for ind in indexes:
    word += S[ind-1]
print(word)

    
    
