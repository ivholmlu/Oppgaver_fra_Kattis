# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:10:04 2021

@author: Ivar
"""

"""

DICE CUP

Differanse mellom terningene pluss 1 mulige utfall? 
Snittet mellom dem som midpunkt i verdier som skal printes ut?

link: https://open.kattis.com/problems/dicecup
"""

line = input()
line = line.split()
D1 = int(line[0])
D2 = int(line[1])

diff = abs(D1-D2)

snitt = int((D1 + D2)/2)

if diff > D1 or D2:
    laveste = min(D1, D2)
    hoyeste = max(D1, D2)
    verdier = range(hoyeste-laveste, hoyeste)

else : 
    verdier = range(int(snitt+1-(diff/2)), int(snitt+2+(diff/2)))

for i in verdier:
    print(round(i))



