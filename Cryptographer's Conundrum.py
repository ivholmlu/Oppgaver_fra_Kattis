"""


Sjekker om p, e og r er riktig plassert.
Om det er det trekkes det fra en dag i antall dager/lengde av ordet.


"""

N = input()
lengde = len(N)
teller = 0
for x, char in enumerate(N):


    if char == 'P':
        for x1 in range(1, len(N)+1, 3):
            if x1 == x+1:
                teller += 1
    elif char == 'E':
        for x1 in range(2, len(N)+2, 3):
            if x1 == x+1:
                teller += 1
    elif char == 'R':
        for x1 in range(3, len(N)+2, 3):
            if x1 == x+1:
                teller += 1
print(lengde-teller)





