# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 00:40:47 2021

@author: Ivar
"""
def sort_two_numbers():
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    if a >= b:
        print(f'{b} {a}')
    else: 
        print(f'{a} {b}')
    
sort_two_numbers()
    
    
    