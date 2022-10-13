N = int(input())
for _ in range(N):
    a = input()
    if a == 'P=NP':
        print('skipped')
    else:
        sum = int(a[0])+int(a[2])
        print(sum)
