
N = int(input())

X = [int(j) for j in input().split()]
Y = [int(j) for j in input().split()]

for x in X:
    if x not in Y:
        print(x)
