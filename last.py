N = int(input())

for _ in range(N):
    fact = int(input())
    x = 1
    for i in range(1, fact+1):
        x = x*i
    x = str(x)
    print(x[-1])

