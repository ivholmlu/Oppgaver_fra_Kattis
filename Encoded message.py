import numpy as np
N = int(input())

for _ in range(N):
    s = input()
    a = int(np.sqrt(len(s)))
    square = [[]]*a
    for x, _ in enumerate(range(a)):
        square[x] = s[x*a:(x+1)*a].split()
    kvadrat = np.array(square)
    print(np.size(kvadrat))
    firkant = np.rot90(kvadrat, k=2, axes = (0, 1))
    print(firkant)





