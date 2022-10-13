# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:19:16 2021

@author: Ivar
"""

nm = input()
nm = nm.split()
n = int(nm[0])
m = int(nm[1])
handleliste = {}

for i in range(n):
    i = input()
    i = i.split()
    
    for j in i:
        if j in handleliste.keys():
            handleliste[j] += 1
        else:
            handleliste[j] = 1

[key for (key, value) in handleliste.items() if value in handleliste] 
handleliste1 = [key for (key, value) in handleliste.items() if value == n]
handleliste1 = sorted(list(handleliste1))
print(len(handleliste1))
for vare in handleliste1:
    print(vare)


# bread carrots cheese eggs milk
# milk carrots bread pasta yogurt
# corn bread kale spinach carrots
# milk bread cheese carrots yogurt