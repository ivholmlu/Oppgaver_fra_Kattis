from math import cos, sin, radians
N = int(input())
# v0 is the initial velocity
# theta is the angle of the cannon
# x1 is the distance to the wall
# h2 is the height of the wall


for n in range(N):
    v0, theta, x1, h1, h2 = [float(x) for x in input().split()]
    theta = radians(theta)
    t = x1/(v0*cos(theta))
    y = v0*t*sin(theta) - 0.5*9.81*t**2

    if y > h1 + 1 and y < h2 - 1:
        print('Safe')
    else:
        print("Not Safe")

