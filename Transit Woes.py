s, t, n = [int(j) for j in input().split()]


time = 0
for i in range(3):
    times = [int(j) for j in input().split()]
    time += sum(times)

if time > t:
    print('no')
else:
    print('yes')
