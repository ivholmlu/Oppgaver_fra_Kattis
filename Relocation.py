
N, Q = [int(j) for j in input().split()]

companies = {}
plassering = [int(j) for j in input().split()]
for i in range(1, N+1):
    companies[i] = plassering[i-1]

for i in range(Q):
    i = [int(j) for j in input().split()]
    if i[0] == 1:
        companies[i[1]] = i[2]
    else:
        distance = 0
        lengde_1 = companies[i[1]]
        lengde_2 = companies[i[2]]
        print(abs(lengde_2-lengde_1))



