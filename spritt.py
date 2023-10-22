n_rooms, bottles = [int(x) for x in input().split()]
count_bottles_needed = 0
for i in range(n_rooms):
    i = int(input())
    count_bottles_needed += i

if count_bottles_needed > bottles:
    print('Neibb')
else:
    print('Jebb')