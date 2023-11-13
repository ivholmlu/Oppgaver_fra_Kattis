
not_dominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}

summ = 0
N, B = input().split()
N = int(N)

for i in range(int(4*N)):
    card = input()
    if card[1] == B:
        summ += dominant[card[0]]
    else:
        summ += not_dominant[card[0]]
print(summ)