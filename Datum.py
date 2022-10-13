import calendar

yy = 2009

D, M = [int(j) for j in input().split()]

a = calendar.weekday(yy, M, D)

if a == 0:
    print('Monday')
elif a == 1:
    print('Tuesday')
elif a == 2:
    print('Wednesday')
elif a == 3:
    print('Thursday')
elif a == 4:
    print('Friday')
elif a == 5:
    print('Saturday')
else:
    print('Sunday')
