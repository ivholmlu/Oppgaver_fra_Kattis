m = int(input())
shapes = []

def check_square(sx, sy, x1, y1, x2, y2):
    """
    Check if a point (sx, sy) is within a square defined
    by its bottom-left corner (x1, y1) and top-right corner (x2, y2).
    """
    return x1 <= sx <= x2 and y1 <= sy <= y2

def check_circle(sx, sy, x1, y1, r):
    """
    Link for formula: https://doubleroot.in/lessons/circle/position-of-a-point/
    """
    return (sx - x1)**2 + (sy - y1)**2 <= r**2


for shape in range(m):
    shapes.append([int(i) if x != 0 else i for x, i in enumerate(input().split())])

n_shots = int(input())

for shot in range(n_shots):
    count = 0
    sx, sy = [int(x) for x in input().split()]
    for shape in shapes:
        if shape[0] == "rectangle":
            if check_square(sx, sy, shape[1], shape[2], shape[3], shape[4]):
                count += 1
        else:
            if check_circle(sx, sy, shape[1], shape[2], shape[3]):
                count += 1
    print(count)
