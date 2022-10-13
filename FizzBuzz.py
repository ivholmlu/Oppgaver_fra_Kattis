# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:45:38 2021

@author: Ivar
"""
"""
feil per nå, alt blir int siden det er satt int() foran == i if test
Løsning, sjekke siste verdi i stringen. Er det 0 så er det heltall,
ellers blir float.

"""

# line = input()
# line = line.split()
# X = int(line[0])
# Y = int(line[1])
# N = int(line[2])

# for i in range(1, N+1):
#     test_x = i/X
    
#     test_y = i/Y
#     if type(test_x) == int and type(test_y) == float:
#         print('Fizz')
#     elif type(test_x) == float and type(test_y) == int:
#         print('Buzz')
#     elif type(test_x) == int and type(test_y) == int:
#         print('FizzBuzz')
#     else:
#         print(i)


x, y, N = [int(j) for j in input().split()]

for i in range(1, N+1):
    
    if str(i/x)[-1] == '0':
        if str(i/y)[-1]=='0':
            print('FizzBuzz')
        else:
            print('Fizz')
    elif str(i/y)[-1] == '0':
        print('Buzz')
    else:
        print(i)
    
        
        

    
    





