number_of_stats = int(input())
stats = [int(input()) for i in range(number_of_stats)]
stats_of_brothers = [stats.copy(), stats.copy()]
number_of_trains = int(input())
for i in range(number_of_trains):
    brother = int(input()) - 1
    stat = int(input())
    stat_increase = int(input())
    stats_of_brothers[brother][stat] += stat_increase
for item in stats_of_brothers:
    print(*item)
print(len(set(stats_of_brothers[0]) & set(stats_of_brothers[1])))