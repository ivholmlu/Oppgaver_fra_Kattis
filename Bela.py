# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:12:54 2021

@author: Ivar
"""

"""
Kode som kan telle poeng i Bela-spillet

FUngerer på første sample input men ikke resten??
Finner ingen åpenbar feil

link: https://open.kattis.com/problems/bela
"""

line1 = input().split()
n = int(line1[0])
trump_value = line1[1]
print(trump_value)
sum1 = 0
for i in range(4*n):
    card = input()
    
    if card[1] == trump_value:
        
        if card[0] == 'A':
            sum1 += 11
        elif card[0] == 'K':
            sum1 += 4
        elif card[0] == 'Q':
            sum1 += 3
        elif card[0] == 'J':
            sum1 += 20
        elif card[0] == 'T':
            sum1 += 10
        elif int(card[0]) == 9:
            sum1 += 14
        elif int(card[0]) == 8:
            sum1 += 0
        elif int(card[0]) == 7:
            sum1 += 0
    
    elif card[1] != trump_value:
         if card[0] == 'A':
            sum1 += 11
         elif card[0] == 'K':
            sum1 += 4
         elif card[0] == 'Q':
            sum1 += 3
         elif card[0] == 'J':
            sum1 += 2
         elif card[0] == 'T':
            sum1 += 10
         elif int(card[0]) == 9:
            sum1 += 0
         elif int(card[0]) == 8:
            sum1 += 0
         elif int(card[0]) == 7:
            sum1 += 0


print(sum1)
        
        
    
    
    
    