# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:55:18 2021

@author: Ivar
"""


import math as m

h, v = [int(j) for j in input().split()]

hyp = h/m.sin(m.radians(v))

print(m.ceil(hyp))