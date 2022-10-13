N = int(input())
a = 0
for i in range(N):
    i = input().lower()
    if 'pink' in i:
        a += 1
    elif 'rose' in i:
        a += 1
if a == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(a)

