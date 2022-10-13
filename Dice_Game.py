# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 00:13:34 2021

@author: Ivar
"""

(Ga1, Gb1, Ga2, Gb2) = input().split()
(Ea1, Eb1, Ea2, Eb2) = input().split()


forventning_Gunnar1 = int(Ga1)+(int(Gb1)-int(Ga1)/2)

forventning_Emma1 = int(Ea1)+((int(Eb1)-int(Ea1))/2)

forventning_Gunnar = int(Ga2)+(int(Gb2)-int(Ga2)/2) + forventning_Gunnar1

forventning_Emma = int(Ea2)+((int(Eb2)-int(Ea2))/2) + forventning_Emma1

if forventning_Emma > forventning_Gunnar:
    print('Emma')

elif forventning_Emma == forventning_Gunnar:
    print('Tie')
else:
    print('Gunnar')




