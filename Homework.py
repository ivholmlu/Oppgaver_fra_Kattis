# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:56:25 2021

@author: Ivar
"""

"""
; separer oppgaver
- viser til alle imellom og tallene som binder

returnere liste med verdiene


"""
line = input()
sum_oppgaver = 0

for char in line:
    try:
        if int(char) == type(int):
            sum_oppgaver += int(char)
        
        elif char == ';' or '-':
            char = char
    
    except:
        char = char
    
print(sum_oppgaver)
    

