max_w_speed = int(input())
N = int(input())

for i in range(N):
    name, max_speed = input().split()
    max_speed = int(max_speed)
    if max_speed >= max_w_speed:
        print(f"{name} opin")
    else:
        print(f"{name} lokud")