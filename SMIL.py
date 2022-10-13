# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:22:37 2021

@author: Ivar
"""

"""

Finne smil i en lang liste med input separert av blank space

Print med :-) funker dårlig mtp indeksering

Slet med å bruke or og and i if-testinga

Link: https://open.kattis.com/problems/smil
"""
#Enumerate????
n = input()

for x, char in enumerate(n):
    try: 
        if char == ':':
            if n[x+1] == ')':
                print(x)
            elif n[x+1] == '-':
                if n[x+2] == ')':
                    print(x)
            else:
                char = char
        else:
            char = char
            
        if char == ';':
            if n[x+1] == ')':
                print(x)
            elif n[x+1] == '-':
                if n[x+2] == ')':
                    print(x)
            else:
                char = char
        else:
            char = char
            
    except: 
        char=char
        
        
        