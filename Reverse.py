# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:46:44 2021

@author: Ivar
"""
""
# REVERSE
""
"""
Kode som printer ut unike verdier i synkende rekkefølge
Alle input er n integers.

5 -antall
[1, 2, 3, ,4, 5] - kan være usortert

"""
#ALTERNATIV 1
n = int(input())
list_n = []
for i in range(n):
    list_n.append(input())



def int_descending_order(list_n):
    
    
    list_n = set(list_n)
    
    list_n = list(list_n)
    
    list_n = sorted(list_n, reverse = True)
    
    return list_n


ns = int_descending_order(list_n)
for i in ns:
    print(i)
#%%    
#Alternativ 2, fungerer best
n = int(input()) #Finner lengden
list_n = []
for i in range(n):
    
    list_n.append(int(input()))

for i in range(1, n+1):
    
    
    print(list_n[-i])


    

    
    





    
    