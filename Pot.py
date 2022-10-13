# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:05:49 2021

@author: Ivar
"""

"""
Kode som tar siste verdi i tallet og opphøyer med den verdien.
"""

n= int(input())
sum1 = 0
for i in range(n):
    line = input()
    faktor = line[-1]
    sum1 += int(line[:-1])**int(line[-1])
    
print(sum1)


    
    