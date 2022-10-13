N = int(input())

for i in range(N):
    a = int(input())
    if a % 2 != 0:
        print(f'{a} is odd')
    else:
        print(f'{a} is even')