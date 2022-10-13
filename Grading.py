A, B, C, D, E = [int(i) for i in input().split()]

p_score = int(input())

if p_score >= A:
    print('A')
elif p_score<A and p_score >= B:
    print('B')
elif p_score<B and p_score >= C:
    print('C')
elif p_score<C and p_score >= D:
    print('D')
elif p_score<D and p_score >= E:
    print('E')
else:
    print('F')
