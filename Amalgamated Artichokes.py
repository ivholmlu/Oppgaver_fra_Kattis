# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:05:50 2021

@author: Ivar
"""

import math as m
line_values = input().split()
p = int(line_values[0])
a = int(line_values[1])
b = int(line_values[2])
c = int(line_values[3])
d = int(line_values[4])
k_max = int(line_values[5])

highest_price = 0
highest_difference = 0
for k in range(1, k_max+1):
    price = p*(m.sin(a*k+b)+m.cos(c*k+d)+2)
    if price>highest_price:
        highest_price = price
    highest_difference1 = highest_price-price 
    if highest_difference < highest_difference1:
        highest_difference = highest_difference1
          
print(highest_difference)
