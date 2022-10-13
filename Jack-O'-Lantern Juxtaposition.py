# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:48:58 2021

@author: Ivar
"""

line = input()
line = line.split()

eye_comb = line[0]
nose_comb = line[1]
mouth_comb = line[2]

print(eye_comb*nose_comb*mouth_comb)