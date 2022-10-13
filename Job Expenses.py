

N = int(input())

verdier = [int(j) for j in input().split()]
utgifter = 0
for i in verdier:
    if i<0:
        utgifter += i*(-1)
print(utgifter)
