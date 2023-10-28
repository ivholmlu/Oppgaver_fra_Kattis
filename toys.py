"""Link: https://open.kattis.com/problems/toys"""


T, K = [int(i) for i in input().split()]

T = list(range(T))
count = 0
current_index = K-1
del T[current_index]
while len(T)>1:
    
    if current_index+K>len(T)-1:
        current_index = K - (len(T)-current_index-1)
    else:
        current_index += K
    
    print("Current list and length:")
    print(T, len(T))
    print("Current index:")
    print(current_index)
    print("removed value:")
    print(T[current_index])
    del T[current_index]
print(T[0])


    
