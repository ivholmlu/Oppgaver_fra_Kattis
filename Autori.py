S = input()

initialer = [S[0]]

for x, char in enumerate(S):
    if char == '-':
        initialer.append(S[x+1])

print(''.join(initialer))