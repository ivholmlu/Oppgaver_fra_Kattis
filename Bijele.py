
fasit = [1, 1, 2, 2, 2, 8]

gjeldende = [int(j) for j in input().split()]

mangler = []

for x, numb in enumerate(gjeldende):
    i = fasit[x]-numb
    mangler.append(str(i))

print(' '.join(mangler))