# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:39:08 2021

@author: Ivar
"""

"""
Bruke dictionary for å lagre datoen med størst value
Går ikke? Er 3 inputs man er avhengig av.

Funker, men litt rotete.
Sikkert en måte å sortere dictionaryen på, evt ikke lagre values som en 
liste slik at det blir lettere å printe ut i riktig rekkefølge
"""


N = int(input())

bursdager = {}

for i in range(N):
    liste = input().split()
    navn = liste[0]
    poeng = int(liste[1])
    dato = liste[2]
    if dato not in bursdager:
        bursdager[dato] = poeng, navn
    
    if poeng>bursdager[dato][0]:
        bursdager[dato] = poeng, navn
    
print(len(bursdager))
navne_liste = []
for keys, values in bursdager.items():
    navne_liste.append(values[1])
        
navne_liste = sorted(navne_liste)

for navn in navne_liste:
    print(navn)
            
    
         #Sliter med å finne fram navn og dato på en gang
        