# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:25:09 2021

@author: Ivar
"""

"""
Lager dict med antallet kort som har bestemt verdi
"""

liste = input().split()
kort_dict = {}

for x, i in enumerate(liste):
    if i[0] in kort_dict:
        kort_dict[i[0]] += 1
    else:
        kort_dict[i[0]] = 1

a = max(kort_dict, key=kort_dict.get)
print(kort_dict[a])
    
    
    


    
    