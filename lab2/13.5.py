number_of_teams = int(input())
teams = []
average = 0
for i in range(number_of_teams):
    teams.append((input(), int(input())))
for team in teams:
    average += team[1]
average /= len(teams)
list_of_teams = list(teams)
list_of_teams.sort(key=lambda x: x[0])
for team in list_of_teams:
    if team[1] > average:
        print(team[0])
        list_of_teams.remove(team)
print(*(team[0] for team in list_of_teams), sep='\n')