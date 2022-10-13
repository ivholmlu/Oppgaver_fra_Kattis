N = int(input())


for i in range(N):
    a = input()
    b = input()
    lik_test = []
    for x, char in enumerate(a):
        if b[x] == char:
            lik_test.append('.')
        else:
            lik_test.append('*')
    print(a)
    print(b)
    print(''.join(lik_test))
