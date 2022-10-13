

x = []
y = []
for _ in range(3):
    xn, yn = [int(j) for j in input().split()]
    x.append(xn)
    y.append(yn)
x4 = 0
y4 = 0
x.sort()
y.sort()

if x[0] == x[1]:
    x4 = x[2]
else:
    x4 = x[0]
if y[0] == y[1]:
    y4 = y[2]
else:
    y4 = y[0]


print(x4, y4)
