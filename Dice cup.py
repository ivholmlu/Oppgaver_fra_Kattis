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

N, M= [int(x) for x in input().split()]
diff = abs(N-M)
for x, _ in enumerate(range(diff+1), 1):
    print(min(N, M)+x)







