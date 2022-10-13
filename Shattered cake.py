W = int(input())
N = int(input())
Areal = 0
for _ in range(N):
    x, y = [int(x) for x in input().split()]
    Areal += x*y

print(int(Areal/W))
