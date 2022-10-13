
N = input()

whitespace = 0
sma = 0
store = 0
symboler = 0

for char in N:

    if char.isupper():
        store += 1
    elif char.islower():
        sma += 1
    elif char == '_':
        whitespace += 1
    else:
        symboler += 1

antall = len(N)
print(whitespace/antall, sma/antall, store/antall, symboler/antall)
