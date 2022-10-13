N = int(input())
steps = 0
if N==2:

    steps += 6

elif N == 3:

    steps += 12

elif N == 4:

    steps += 90
elif N > 4:
    pass


#Prøver på noe annet her

muligheter = 6
counter = 0

for _ in range(N):
    if counter <= N/2:
        multiplier = 4
    if N-

