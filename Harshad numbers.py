

N = input()

initial = False

while initial == False:
    N = str(N)
    N_liste_int = [int(j) for j in N]
    sum1 = 0
    sum1 = sum(N_liste_int)
    if str(int(N)/sum1)[-1] == '0':
        initial = True
        print(N)
    else:
        N = int(N)
        N += 1





