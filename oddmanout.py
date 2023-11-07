N = int(input())


for i in range(N):
    G = int(input())
    values = [int(x) for x in input().split()]
    for value in values:
        if values.count(value) == 1:
            print(f"Case #{i+1}: {value}")
            break
        