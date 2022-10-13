N = int(input())
winners = []
schools = []
for i in range(N):
    team = input()
    school = team.split()
    if school[0] not in schools:
        schools.append(school[0])
        winners.append(team)

for i in range(12):
    print(winners[i])

