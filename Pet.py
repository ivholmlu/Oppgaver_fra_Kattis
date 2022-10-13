
N = 5
winner_score = 0
for i in range(5):
    participant = i+1
    paricipant_score = 0

    list_score = [int(j) for j in input().split()]

    if sum(list_score) > winner_score:
        winner_score = sum(list_score)
        winner = participant

print(winner, winner_score)
