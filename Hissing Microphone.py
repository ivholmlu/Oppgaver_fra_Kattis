N = input()
a = 0
for x, char in enumerate(N):
    if char.lower() == 's':
        try:
            if N[x+1] == 's':
                a = 1
        except:
            pass
if a == 1:
    print('hiss')
else:
    print('no hiss')

