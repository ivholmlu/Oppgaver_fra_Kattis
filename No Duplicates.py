N_words = input().split()


a = 0
sjekk = []
for word in N_words:
    if word in sjekk:
        a = 1
    else:
        sjekk.append(word)
if a == 1:
    print('no')
else:
    print('yes')



