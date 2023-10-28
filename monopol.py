#link to problem: https://open.kattis.com/problems/monopol

N = int(input())

numbers = [int(i) for i in input().split()]

accumulated_prob = 0
for num in numbers:
    
    prob = 6-abs(7-num)

    dice_prob = prob/6 * 1/6
    accumulated_prob += dice_prob
print(accumulated_prob)


