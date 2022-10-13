import math as m
n = int(input())
t_1 = 1
d_1 = 0
mspeed = 0
speed = 0
for i in range(n):

    t, d = [int(j) for j in input().split()]

    distanse = d-d_1
    tid = t-t_1
    speed = distanse / tid
    if speed > mspeed:
        mspeed = speed
    t_1 = t
    d_1 = d
print(m.floor(mspeed))

