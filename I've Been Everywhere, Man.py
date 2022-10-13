# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:54:03 2021

@author: Ivar
"""


n = int(input())
dict_cities = {}
for i in range(n):
    i = int(input())
    dict_cities = {}
    for j in range(i):
        j = input()
        if j in dict_cities:
            dict_cities[j] += 1
        dict_cities[j] = 0
    print(len(dict_cities))
    
    