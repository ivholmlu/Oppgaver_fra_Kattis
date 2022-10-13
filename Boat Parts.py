
P, N = [int(x) for x in input().split()]
deler_byttet = []
X = 0

for x, _ in enumerate(range(N)):
    part = input()
    if part not in deler_byttet:
        deler_byttet.append(part)
    X = x

if len(deler_byttet) < P:
    print('paradox avoided')
else:
    print(X)
 