
for _ in range(int(input())):
    test_list = [int(x) for x in input().split()]
    last = 0
    turtles = 0
    for i in (test_list):
        if last*2 < i and last != 0:
            turtles += i - (last*2)
        last = i
    print(turtles)
