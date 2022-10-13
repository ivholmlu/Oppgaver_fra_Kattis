
T, M = [int(j) for j in input().split()]

M1 = M-45

if M1 < 0:
    if T == 0:
        T = 23
        M1 = 60+M1

    else:
        M1 = 60+M1
        T = T-1

print(T, M1)





