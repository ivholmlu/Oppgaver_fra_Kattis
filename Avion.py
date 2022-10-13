list1 = []
str1 = ''
for x, _ in enumerate(range(5)):

    if 'FBI' in input():
        list1.append(x)

if len(list1) ==0:
    print('HE GOT AWAY!')
else:
    print(*list1, sep=" ")